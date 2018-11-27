'''
Created on 2018年11月26日

@author: wanglx
'''
# coding=UTF-8
import pandas as pd
import numpy as np
import csv
from config.properties import SOURCE_DIR
from config.properties import CODE_COMBINATION, ZCE_CODE, DCE_CODE, SHF_CODE
import matplotlib.pyplot as plt


def add_close_difference(df, code1, code2):
    """
    合并两个合约，并添加收盘价差价
    """
    df1 = df[df['ts_code'] == code1][['trade_date', 'close', 'vol', 'oi']].sort_values('trade_date', ascending=True)
    df2 = df[df['ts_code'] == code2][['trade_date', 'close', 'vol', 'oi']].sort_values('trade_date', ascending=True)
    
    df1.columns = ['trade_date', 'close1', 'vol1', 'oi1' ]
    df2.columns = ['trade_date', 'close2', 'vol2', 'oi2' ]
    
    result = pd.merge(df1, df2, on='trade_date', how='inner')
    result[['close1', 'close2', 'vol1', 'vol2', 'oi1', 'oi2']] = result[['close1', 'close2', 'vol1', 'vol2', 'oi1', 'oi2']].apply(pd.to_numeric)
    
    result['difference'] = result['close1'] - result['close2']
#     result['ave_difference'] = np.round(pd.Series.rolling(result['difference'], window=20).mean(), 2)
    return result 


def get_ave_line(column, N):
    """
    返回数据列的均线
    输入为DataFrame的某一列，均线日期
    """
    return np.round(pd.Series.rolling(column, window=N).mean(), 2)


def show(df, code1, code2, N):
    """
    展示两份合约成交量、持仓量、差价及N日差价
    """
    result = add_close_difference(df, code1, code2)
    result['ave_difference%s' % N] = get_ave_line(result['difference'], N)
    plt.figure(1)
    plt.subplot(311)
    plt.plot(result['trade_date'], result['difference'], c='red', label='difference')
    plt.plot(result['trade_date'], result['ave_difference%s' % N], c='blue', label='ave_difference%s' % N)
    plt.legend(loc='upper left')
    plt.subplot(312)
    plt.plot(result['trade_date'], result['oi1'], c='red', label='oi1')
    plt.plot(result['trade_date'], result['oi2'], c='blue', label='oi2')
    plt.legend(loc='upper left')
    plt.subplot(313)
    plt.plot(result['trade_date'], result['vol1'], c='red', label='vol1')
    plt.plot(result['trade_date'], result['vol2'], c='blue', label='vol2')
    plt.legend(loc='upper left')
    plt.show()


def get_code_near_ave(df, N):
    """
    获取某条均线附近的合约及合约组合有哪些
    """
    result = []
    for code in ZCE_CODE:
        df1 = df[df['ts_code'] == code][['trade_date', 'close']].sort_values('trade_date', ascending=True)
        if df1.shape[0] > 0:
            df1['ave_close%s' % N] = get_ave_line(df1['close'], N)
            df1['close'] = df1['close'].apply(pd.to_numeric)
            if df1['ave_close%s' % N].iat[-1] * 0.9 < df1['close'].iat[-1] < df1['ave_close%s' % N].iat[-1] * 1.1 :
                result.append(code)

    for code in DCE_CODE:
        df1 = df[df['ts_code'] == code][['trade_date', 'close']].sort_values('trade_date', ascending=True)
        if df1.shape[0] > 0:
            df1['ave_close%s' % N] = get_ave_line(df1['close'], N)
            df1['close'] = df1['close'].apply(pd.to_numeric)
            if df1['ave_close%s' % N].iat[-1] * 0.9 < df1['close'].iat[-1] < df1['ave_close%s' % N].iat[-1] * 1.1 :
                result.append(code)
            
    for code in SHF_CODE:
        df1 = df[df['ts_code'] == code][['trade_date', 'close']].sort_values('trade_date', ascending=True)
        if df1.shape[0] > 0:
            df1['ave_close%s' % N] = get_ave_line(df1['close'], N)
            df1['close'] = df1['close'].apply(pd.to_numeric)
            if df1['ave_close%s' % N].iat[-1] * 0.9 < df1['close'].iat[-1] < df1['ave_close%s' % N].iat[-1] * 1.1 :
                result.append(code)
            
    for codes in CODE_COMBINATION:
        code1 = codes[0]
        code2 = codes[1]
        df1 = add_close_difference(df, code1, code2)
        if df1.shape[0] > 0:
            df1['ave_close%s' % N] = get_ave_line(df1['difference'], N)
            if df1['ave_close%s' % N].iat[-1] * 0.9 < df1['difference'].iat[-1] < df1['ave_close%s' % N].iat[-1] * 1.1 :
                result.append(codes)
    
    print(result)
    return result


if __name__ == '__main__':
    
    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    code1 = 'C 01'
    code2 = 'C 05'
    N = 60
    get_code_near_ave(df_source, N)
#     show(df_source, code1, code2, N)
    
