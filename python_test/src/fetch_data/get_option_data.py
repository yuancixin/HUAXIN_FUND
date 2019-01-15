# coding=UTF-8
'''
Created on 2019年1月14日

@author: wanglx
'''
import tushare as ts
import pandas as pd
import datetime
import time
import os
import csv
from config.properties import SOURCE_DIR, TOKEN


def get_trade_cal(pro, start_date, end_date):
    """
    获取各大交易所交易日历数据,默认提取的是上交所
    """
    trade_days = pro.trade_cal(exchange='', start_date=start_date, end_date=end_date)
    return trade_days[trade_days['is_open'] == 1]['cal_date']


def get_code_list(pro):
    """
    查询当前所有的期权合约信息
    """
    print('---获取当前所有的期权合约信息---')
    exchange_list = ['SSE', 'CZCE', 'SHFE', 'DCE']
    result = pd.DataFrame()
    for exchange in exchange_list:
        option_baseinfo = pro.opt_basic(exchange=exchange)
        result = result.append(option_baseinfo)
    result.to_csv('%s/option_baseinfo.csv' % SOURCE_DIR, index=0, encoding='utf-8')


def get_day_daily(pro, trade_date):
    """
    获取某日所有期权的日线行情
    """
    df = pro.opt_daily(trade_date=trade_date)
    return df


def main():
    """
    2015年2月9日，上证50ETF期权于上海证券交易所上市，是国内首只场内期权品种。
    期权数据接口每分钟最多访问该接口10次
    """
    start_date = '20150209'
    if os.path.exists('%s/option_data.csv' % SOURCE_DIR):
        df_source = pd.read_csv('%s/option_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
        start_date = str(df_source['trade_date'].max())
    else:
        print('---未检测到期权数据文件，准备全量下载---')
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    if start_date == end_date:
        print('---期权数据已是最新---')
    else:
        print('---开始爬取期权数据！---')
        pro = ts.pro_api(TOKEN)  # 设定TOKEN 
        get_code_list(pro)     
        trade_days = get_trade_cal(pro, start_date, end_date)
        count = 0
        for trade_date in trade_days:
#             接口每分钟最多访问该接口10次
            if count >= 10:
                count = 0
                print('---每分钟最多访问该接口10次,等待一分钟。---')
                time.sleep(60)
            print('%s爬取开始' % trade_date)
            daily_data = get_day_daily(pro, trade_date)
            daily_data.to_csv('%s/option_data.csv' % SOURCE_DIR, header=not os.path.exists('%s/option_data.csv' % SOURCE_DIR), mode='a', index=0, encoding='utf-8')
            count = count + 1
        print('---期权数据爬取完成，开始数据清洗---')
        df_source = pd.read_csv('%s/option_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
        df_source.sort_values(by=['ts_code', 'trade_date'], ascending=(True, True), inplace=True)
        df_source.drop_duplicates(subset=['ts_code', 'trade_date'], keep='first', inplace=True)
        df_source.to_csv('%s/option_data.csv' % SOURCE_DIR, index=0, encoding='utf-8')
        print('---期权日线行情数据已是最新---')


if __name__ == '__main__': 
    main()
