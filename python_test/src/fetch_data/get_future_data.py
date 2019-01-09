# coding=UTF-8
import tushare as ts
import pandas as pd
import datetime
import os
import time
import csv
from config.properties import ZCE_CODE, DCE_CODE, SHF_CODE, TOKEN
from config.properties import SOURCE_DIR


def get_code_daily(pro, ts_code, start_date, end_date):
    """
    根据 合约代码 获取 交易日区间 期货日线行情
    """
    df = pro.fut_daily(ts_code=ts_code, start_date=start_date, end_date=end_date,
                       fields='ts_code,trade_date,close,oi,vol')
    return df


def get_all_daily(pro, start_date, end_date, year_code):
    """
    按年份 获取 三大交易所 交易日区间 期货日线行情
    """
    result = pd.DataFrame()
    print('ZCE开始')
    for code in ZCE_CODE:
        df = get_code_daily(pro, '%s.ZCE' % code.replace(" ", year_code), start_date, end_date)
        df['ts_code'] = code
        df['year'] = year_code
        result = result.append(df)
    print('DCE开始')
    for code in DCE_CODE:
        df = get_code_daily(pro, '%s.DCE' % code.replace(" ", year_code), start_date, end_date)
        df['ts_code'] = code
        df['year'] = year_code
        result = result.append(df)
    time.sleep(60)
    print('SHF开始')
    for code in SHF_CODE:
        df = get_code_daily(pro, '%s.SHF' % code.replace(" ", year_code), start_date, end_date)
        df['ts_code'] = code
        df['year'] = year_code
        result = result.append(df)
    return result


def get_trade_cal(pro, start_date, end_date):
    """
    获取各大期货交易所交易日历数据
    """
    trade_days = pro.trade_cal(exchange='DCE', start_date=start_date, end_date=end_date)
    return trade_days[trade_days['is_open'] == 1]['cal_date']


def get_day_daily(pro, trade_date):
    """
    获取某日所有期货的日线行情
    """
    df = pro.fut_daily(trade_date=trade_date, exchange='', fields='ts_code,trade_date,close,oi,vol')
    df['ts_code'] = df['ts_code'].apply(lambda x: x.split('.')[0])
    df = df[df['ts_code'].str.len() > 4]
    df['year'] = df['ts_code'].str[-4:-2].apply(pd.to_numeric)
    df['ts_code'] = df['ts_code'].str.slice_replace(-4, -2, " ")
    code = ZCE_CODE + DCE_CODE + SHF_CODE
    df = df[df["ts_code"].isin(code)]
    return df


def clean_data():
    """
    数据去重、缺失值填充
    """
    print('---开始数据去重!---')
    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    code = ZCE_CODE + DCE_CODE + SHF_CODE
    df_source = df_source[df_source["ts_code"].isin(code)]
    df_source.sort_values(by=['ts_code', 'trade_date', 'year'], ascending=(True, True, True), inplace=True)
    df_source.drop_duplicates(subset=['ts_code', 'trade_date'], keep='first', inplace=True)
    df_source = df_source.reset_index(drop=True)
    print('---期货数据去重完成---')
    print('---开始缺失值填充!---')
    null_index = df_source[pd.isnull(df_source['close'])].index.tolist()
    for i in null_index:
        if i > 0:
            df_source.loc[i, 'close'] = df_source.loc[i - 1, 'close']
        else:
            df_source.loc[i, 'close'] = 0
    df_source.to_csv('%s/future_data.csv' % SOURCE_DIR, index=0, encoding='utf-8')


def add_new(add_zce_code, add_dce_code, add_shf_code):
    
    def get_all_add_daily(pro, start_date, end_date, year_code, add_zce_code, add_dce_code, add_shf_code):
        """
        按年份 获取 给定合约代码 交易日区间 期货日线行情
        """
        result = pd.DataFrame()
        print('ZCE开始')
        for code in add_zce_code:
            df = get_code_daily(pro, '%s.ZCE' % code.replace(" ", year_code), start_date, end_date)
            df['ts_code'] = code
            df['year'] = year_code
            result = result.append(df)
        print('DCE开始')
        for code in add_dce_code:
            df = get_code_daily(pro, '%s.DCE' % code.replace(" ", year_code), start_date, end_date)
            df['ts_code'] = code
            df['year'] = year_code
            result = result.append(df)
        print('SHF开始')
        for code in add_shf_code:
            df = get_code_daily(pro, '%s.SHF' % code.replace(" ", year_code), start_date, end_date)
            df['ts_code'] = code
            df['year'] = year_code
            result = result.append(df)
        return result

    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    start_date = '20000101'
    end_date = str(df_source['trade_date'].max())
    pro = ts.pro_api(TOKEN) 
    year_code = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    for year in year_code:
        print('%s开始' % year)
        result = get_all_add_daily(pro, start_date, end_date, year, add_zce_code, add_dce_code, add_shf_code)
        result.to_csv('%s/future_data.csv' % SOURCE_DIR, header=not os.path.exists('%s/future_data.csv' % SOURCE_DIR), mode='a', index=0, encoding='utf-8')
        if not year_code[len(year_code) - 1] == year:
            time.sleep(6)
    print('---期货数据爬取完成---')
    clean_data()
    print('---程序结束---')


def main():
    """
    期货数据接口每分钟最多调用120次，单次最大2000条，总量不限制。注意设定好调用频率
    """
    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    
    start_date = str(df_source['trade_date'].max())
#     start_date = '20180101'
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    
    if start_date == end_date:
        print('---期货数据已是最新---')
    else:
        print('---开始爬取期货数据！---')
        pro = ts.pro_api(TOKEN)  # 设定TOKEN      
        trade_days = get_trade_cal(pro, start_date, end_date)
        for trade_date in trade_days:
            print('%s爬取开始' % trade_date)
            daily_data = get_day_daily(pro, trade_date)
            daily_data.to_csv('%s/future_data.csv' % SOURCE_DIR, header=not os.path.exists('%s/future_data.csv' % SOURCE_DIR), mode='a', index=0, encoding='utf-8')
        print('---期货数据爬取完成---')
        clean_data()
        print('---期货数据已是最新---')


if __name__ == '__main__': 
    main()
    
