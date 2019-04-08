# coding=UTF-8
'''
Created on 2018年12月17日

@author: wanglx
'''
import pandas as pd
import numpy as np
import csv
from config.properties import SOURCE_DIR


def get_ave_line(column, N):
    """
    返回数据列的均线
    输入为DataFrame的某一列，均线日期
    """
    return np.round(pd.Series.rolling(column, window=N).mean(), 2)


def get_code_near_ave(df, N, M):
    """
    获取N日均线附近的股票
    """
    result = []
    print("读取数据...")
    df_baseinfo = pd.read_csv('%s/stock_baseinfo.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    all_codes = df_baseinfo['ts_code']
    print("读取数据完成")
    for code in all_codes:
        df1 = df[df['ts_code'] == code][['trade_date', 'close']].sort_values('trade_date', ascending=True)
        if df1.shape[0] > 0:
            df1['ave_close%s' % N] = get_ave_line(df1['close'], N)
            df1['close'] = df1['close'].apply(pd.to_numeric)
            if df1['ave_close%s' % N].iat[-1] * (1 - M) < df1['close'].iat[-1] < df1['ave_close%s' % N].iat[-1] * (1 + M) :
                result.append(code)
    
    print('%s日均线附近 %s%% 的合约：' % (N, M * 100))
    print(result)
    return result


if __name__ == '__main__':
    
    df_source = pd.read_csv('%s/stock_daily_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    strat_date = 20180101
    end_date = 20181231
    df_source = df_source[df_source['trade_date'] > strat_date][['ts_code','trade_date','close']]
    
    N = 120
    M = 0.01
    get_code_near_ave(df_source, N, M)
