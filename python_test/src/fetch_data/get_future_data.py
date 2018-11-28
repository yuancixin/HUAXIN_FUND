# coding=UTF-8

import tushare as ts
import pandas as pd
import os
import time
import csv
from config.properties import ZCE_CODE, DCE_CODE, SHF_CODE, TOKEN
from config.properties import SOURCE_DIR


def get_code_daily(ts_code, start_date, end_date):
    """
    根据 合约代码 获取 交易日区间 期货日线行情
    """
    df = pro.fut_daily(ts_code=ts_code, start_date=start_date, end_date=end_date,
                       fields='ts_code,trade_date,close,oi,vol')
    return df


def get_all_daily(start_date, end_date, year_code):
    """
    按年份 获取 三大交易所 交易日区间 期货日线行情
    """
    result = pd.DataFrame()
    print('ZCE开始')
    for code in ZCE_CODE:
        df = get_code_daily('%s.ZCE' % code.replace(" ", year_code[1]), start_date, end_date)
        df['ts_code'] = code
        df['year'] = year_code
        result = result.append(df)
    print('DCE开始')
    for code in DCE_CODE:
        df = get_code_daily('%s.DCE' % code.replace(" ", year_code), start_date, end_date)
        df['ts_code'] = code
        df['year'] = year_code
        result = result.append(df)
    print('SHF开始')
    for code in SHF_CODE:
        df = get_code_daily('%s.SHF' % code.replace(" ", year_code), start_date, end_date)
        df['ts_code'] = code
        df['year'] = year_code
        result = result.append(df)
    return result


if __name__ == '__main__': 
    """
    期货数据接口每分钟最多调用120次，单次最大2000条，总量不限制。注意设定好调用频率
    """
    
    start_date = '20010101'
    end_date = '20181126'
    year_code = ['13', '14', '15', '16', '17', '18', '19', '20']
    
    print('---程序开始，开始爬取期货数据！---')
    pro = ts.pro_api(TOKEN)  # 设定TOKEN
    for year in year_code:
        print('%s开始' % year)
        result = get_all_daily(start_date, end_date, year)
        result.to_csv('%s/future_data.csv' % SOURCE_DIR, header=not os.path.exists('%s/future_data.csv' % SOURCE_DIR), mode='a', encoding='utf-8')
        time.sleep(60)
    print('---爬取期货数据结束,正在进行数据去重!---')
    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    df_source.sort_values(by=['ts_code', 'trade_date', 'year'], ascending=(True, True, True), inplace=True)
    df_source.drop_duplicates(subset=['ts_code', 'trade_date'], keep='first', inplace=True)
    df_source.drop('Unnamed: 0', axis=1, inplace=True)
    df_source.to_csv('%s/future_data.csv' % SOURCE_DIR, encoding='utf-8')
    print('---程序结束---')
    
