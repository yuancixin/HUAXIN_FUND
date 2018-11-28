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
import datetime

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
    return result 


def get_ave_line(column, N):
    """
    返回数据列的均线
    输入为DataFrame的某一列，均线日期
    """
    return np.round(pd.Series.rolling(column, window=N).mean(), 2)


def get_code_near_ave(df, N, M):
    """
    获取N日均线附近的合约及合约组合
    N:均线日期
    M:均线邻近区间比率
    """
    result = []
    for code in ZCE_CODE:
        df1 = df[df['ts_code'] == code][['trade_date', 'close']].sort_values('trade_date', ascending=True)
        if df1.shape[0] > 0:
            df1['ave_close%s' % N] = get_ave_line(df1['close'], N)
            df1['close'] = df1['close'].apply(pd.to_numeric)
            if df1['ave_close%s' % N].iat[-1] * (1 - M) < df1['close'].iat[-1] < df1['ave_close%s' % N].iat[-1] * (1 + M) :
                result.append(code)

    for code in DCE_CODE:
        df1 = df[df['ts_code'] == code][['trade_date', 'close']].sort_values('trade_date', ascending=True)
        if df1.shape[0] > 0:
            df1['ave_close%s' % N] = get_ave_line(df1['close'], N)
            df1['close'] = df1['close'].apply(pd.to_numeric)
            if df1['ave_close%s' % N].iat[-1] * (1 - M) < df1['close'].iat[-1] < df1['ave_close%s' % N].iat[-1] * (1 + M) :
                result.append(code)
            
    for code in SHF_CODE:
        df1 = df[df['ts_code'] == code][['trade_date', 'close']].sort_values('trade_date', ascending=True)
        if df1.shape[0] > 0:
            df1['ave_close%s' % N] = get_ave_line(df1['close'], N)
            df1['close'] = df1['close'].apply(pd.to_numeric)
            if df1['ave_close%s' % N].iat[-1] * (1 - M) < df1['close'].iat[-1] < df1['ave_close%s' % N].iat[-1] * (1 + M) :
                result.append(code)
            
    for codes in CODE_COMBINATION:
        code1 = codes[0]
        code2 = codes[1]
        df1 = add_close_difference(df, code1, code2)
        if df1.shape[0] > 0:
            df1['ave_close%s' % N] = get_ave_line(df1['difference'], N)
            if df1['ave_close%s' % N].iat[-1] * (1 - M) < df1['difference'].iat[-1] < df1['ave_close%s' % N].iat[-1] * (1 + M) :
                result.append(codes)
    
    print(result)
    return result


def show1(df, code, N):
    """
    展示单份合约收盘价与N日均线
    """
    df1 = df[df['ts_code'] == code][['trade_date', 'close', 'vol', 'oi']].sort_values('trade_date', ascending=True)
    df1['trade_date'] = df1['trade_date'].apply(lambda x: datetime.datetime.strptime(str(x),'%Y%m%d'))
    df1['ave_close%s' % N] = get_ave_line(df1['close'], N)
    plt.plot(df1['trade_date'],df1['close'], c='red', label='close')
    plt.plot(df1['trade_date'],df1['ave_close%s' % N], c='blue', label='ave_close%s' % N)
    plt.legend(loc='upper left')
    plt.suptitle('%s (N=%s)' % (code, N))
    plt.show()


def show2(df, code1, code2, N):
    """
    展示两份合约成交量、持仓量、差价及N日差价
    """
    result = add_close_difference(df, code1, code2)
    result['trade_date'] = result['trade_date'].apply(lambda x: datetime.datetime.strptime(str(x),'%Y%m%d'))
    result['ave_difference%s' % N] = get_ave_line(result['difference'], N)
    result['ave_close1%s' % N] = get_ave_line(result['close1'], N)
    result['ave_close2%s' % N] = get_ave_line(result['close2'], N)
    plt.figure(1)
    plt.subplot(611)
    plt.plot(result['trade_date'],result['difference'], c='red', label='difference')
    plt.plot(result['trade_date'],result['ave_difference%s' % N], c='blue', label='ave_difference%s' % N)
    plt.legend(loc='upper left')
    plt.subplot(612)
    plt.plot(result['trade_date'],result['oi1'], c='red', label='oi1')
    plt.plot(result['trade_date'],result['oi2'], c='blue', label='oi2')
    plt.legend(loc='upper left')
    plt.subplot(613)
    plt.plot(result['trade_date'],result['vol1'], c='red', label='vol1')
    plt.plot(result['trade_date'],result['vol2'], c='blue', label='vol2')
    plt.legend(loc='upper left')
    plt.subplot(614)
    plt.plot(result['trade_date'],result['close1'], c='red', label='close1')
    plt.plot(result['trade_date'],result['close2'], c='blue', label='close2')
    plt.legend(loc='upper left')
    plt.subplot(615)
    plt.plot(result['trade_date'],result['close1'], c='red', label='close1')
    plt.plot(result['trade_date'],result['ave_close1%s' % N], c='blue', label='ave_close1%s' % N)
    plt.legend(loc='upper left')
    plt.subplot(616)
    plt.plot(result['trade_date'],result['close2'], c='red', label='close2')
    plt.plot(result['trade_date'],result['ave_close2%s' % N], c='blue', label='ave_close2%s' % N)
    plt.legend(loc='upper left')
    plt.suptitle('%s and %s (N=%s)' % (code1, code2, N))
    plt.show()


if __name__ == '__main__':
    
    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    
    strat_date = 20150101
    end_date = 20181231
    df_source = df_source[df_source['trade_date'] > strat_date]
    
    N = 60
    M = 0.02
#     result_codes = get_code_near_ave(df_source, N, M)

#     for code in result_codes:
#         if isinstance(code, str):
#             show1(df_source, code, N)
#         else:
#             show2(df_source, code[0], code[1], N)
    show1(df_source, 'RU 01', N)
    show2(df_source, 'C 01', 'C 05', N)
    
