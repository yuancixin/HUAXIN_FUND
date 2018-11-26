# coding=UTF-8

import tushare as ts
import pandas as pd
from config.properties import ZCE, DCE, SHF, TOKEN
from config.properties import SOURCE_DIR


def get_future_data(ts_code, start_date, end_date):
    """
    根据 合约代码 获取 交易日区间 期货日线行情
    """
    df = pro.fut_daily(ts_code=ts_code, start_date=start_date, end_date=end_date,
                       fields='ts_code,trade_date,close,oi,vol')
    return df


def get_all_data(start_date, end_date, year_code):
    """
    按年份 获取 三大交易所 交易日区间 期货日线行情
    """
    
    result = pd.DataFrame()

    print('ZCE开始')
    for code in ZCE:
        df = get_future_data('%s.ZCE' % code.replace(" ", year_code[1]), start_date, end_date)
        df['ts_code'] = code
        result = result.append(df)
    print('DCE开始')
    for code in DCE:
        df = get_future_data('%s.DCE' % code.replace(" ", year_code), start_date, end_date)
        df['ts_code'] = code
        result = result.append(df)
    print('SHF开始')
    for code in SHF:
        df = get_future_data('%s.SHF' % code.replace(" ", year_code), start_date, end_date)
        df['ts_code'] = code
        result = result.append(df)
    return result


if __name__ == '__main__':
    
    """
    期货数据接口每分钟最多调用120次，单次最大2000条，总量不限制。注意设定好调用频率
    """
    print('---期货数据爬取开始---')
    pro = ts.pro_api(TOKEN) #设定TOKEN
    
    start_date = '20010101'
    end_date = '20181125'
    year_code = ['19']
    
    for year in year_code:
        print('%s开始' % year)
        result = get_all_data(start_date, end_date, year)
        result.to_csv('%s/future_data.csv' % SOURCE_DIR, mode='a', encoding='utf-8')
        
    print('---期货数据爬取结束---')
