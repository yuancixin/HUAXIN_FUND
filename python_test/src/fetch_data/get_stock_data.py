# coding=UTF-8

import tushare as ts
import os
from config.properties import TOKEN
from config.properties import SOURCE_DIR


def get_code_list():
    """
    查询当前所有正常上市交易的股票列表
    """
    print('获取当前所有正常上市交易的股票列表')
    stock_baseinfo = pro.stock_basic(exchange='', list_status='L', fields='ts_code,name,industry,market')
    stock_baseinfo.to_csv('%s/stock_baseinfo.csv' % SOURCE_DIR, encoding='utf-8')
    return stock_baseinfo['ts_code']


def get_code_daily(start_date, end_date, code):
    """
    获取某股票日期区间内的日线行情
    """
    df = pro.daily(ts_code=code, start_date=start_date, end_date=end_date)
    return df


def get_day_daily(trade_date):
    """
    获取某日所有股票的日线行情
    """
    df = pro.daily(trade_date=trade_date)
    return df


if __name__ == '__main__':
    """
    首次采集用get_code_daily()，后期按天采集的话用get_day_daily()
    """
    
    start_date = '20010101'
    end_date = '20181126'
    
    print('---程序开始，开始爬取股票数据！---')
    pro = ts.pro_api(TOKEN)  # 设定TOKEN
    code_list = get_code_list()
    for code in code_list:
        print('%s爬取开始' % code)
        daily_data = get_code_daily(start_date, end_date, code)
        daily_data.to_csv('%s/stock_daily_data.csv' % SOURCE_DIR, header=not os.path.exists('%s/stock_daily_data.csv' % SOURCE_DIR), mode='a', encoding='utf-8')
    print('---程序结束---')
        
