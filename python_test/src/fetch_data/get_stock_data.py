# coding=UTF-8
import tushare as ts
import pandas as pd
import datetime
import csv
import os
from config.properties import TOKEN
from config.properties import SOURCE_DIR


def get_code_list(pro):
    """
    查询当前所有正常上市交易的股票列表
    """
    print('---获取当前所有正常上市交易的股票列表---')
    stock_baseinfo = pro.stock_basic(exchange='', list_status='L', fields='ts_code,name,industry,market')
    stock_baseinfo.to_csv('%s/stock_baseinfo.csv' % SOURCE_DIR, index=0, encoding='utf-8')
    return stock_baseinfo['ts_code']


def get_trade_cal(pro, start_date, end_date):
    """
    获取各大交易所交易日历数据,默认提取的是上交所
    """
    trade_days = pro.trade_cal(exchange='', start_date=start_date, end_date=end_date)
    return trade_days[trade_days['is_open'] == 1]['cal_date']


def get_code_daily(pro, start_date, end_date, code):
    """
    获取某股票日期区间内的日线行情
    """
    df = pro.daily(ts_code=code, start_date=start_date, end_date=end_date)
    return df


def get_day_daily(pro, trade_date):
    """
    获取某日所有股票的日线行情
    """
    df = pro.daily(trade_date=trade_date)
    return df


def main():
    """
    自动更新股票数据
    """
    df_source = pd.read_csv('%s/stock_daily_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    
    start_date = str(df_source['trade_date'].max())
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    
    if start_date == end_date:
        print('---股票数据已是最新---')
    else:
        print('---开始更新股票数据！---')
        pro = ts.pro_api(TOKEN)  # 设定TOKEN
        get_code_list(pro)
        trade_days = get_trade_cal(pro, start_date, end_date)
        for trade_date in trade_days:
            print('%s爬取开始' % trade_date)
            daily_data = get_day_daily(pro, trade_date)
            daily_data.to_csv('%s/stock_daily_data.csv' % SOURCE_DIR, header=not os.path.exists('%s/stock_daily_data.csv' % SOURCE_DIR), mode='a', index=0, encoding='utf-8')
        print('---股票数据更新完成,正在进行数据去重!---')
        df_source = pd.read_csv('%s/stock_daily_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
        df_source.sort_values(by=['ts_code', 'trade_date'], ascending=(True, True), inplace=True)
        df_source.drop_duplicates(subset=['ts_code', 'trade_date'], keep='first', inplace=True)
        df_source.to_csv('%s/stock_daily_data.csv' % SOURCE_DIR, index=0, encoding='utf-8')
        print('---股票数据已是最新---')


if __name__ == '__main__':
    main()
        