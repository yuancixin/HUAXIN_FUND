# coding=UTF-8
'''
Created on 2018年11月26日

@author: wanglx
'''
import pandas as pd
import numpy as np
import csv
from config.properties import SOURCE_DIR
from config.properties import CODE_COMBINATION, CODE_COMBINATION2, ZCE_CODE, DCE_CODE, SHF_CODE
from config.parameter import BEST_N, BEST_NM
import matplotlib.pyplot as plt
import datetime


def add_close_difference(df, code1, code2, multiple=1):
    """
    合并两个合约，并添加收盘价差价
    """
    df1 = df[df['ts_code'] == code1][['trade_date', 'close', 'vol', 'oi']].sort_values('trade_date', ascending=True)
    df2 = df[df['ts_code'] == code2][['trade_date', 'close', 'vol', 'oi']].sort_values('trade_date', ascending=True)
    df1.columns = ['trade_date', 'close1', 'vol1', 'oi1' ]
    df2.columns = ['trade_date', 'close2', 'vol2', 'oi2' ]
    result = pd.merge(df1, df2, on='trade_date', how='inner')
    result[['close1', 'close2', 'vol1', 'vol2', 'oi1', 'oi2']] = result[['close1', 'close2', 'vol1', 'vol2', 'oi1', 'oi2']].apply(pd.to_numeric)
    result['difference'] = result['close1'] - result['close2'] * multiple
    return result 


def get_ave_line(column, N):
    """
    返回数据列的均线
    输入为DataFrame的某一列，均线日期
    """
    return np.round(pd.Series.rolling(column, window=N).mean(), 2)


def get_code_near_ave(df, N, M, D=20):
    """
    获取N日均线附近的合约及合约组合
    N:均线日期
    M:均线邻近区间比率
    """
    result = [[], [], [], [], []]
    
    all_codes = ZCE_CODE + DCE_CODE + SHF_CODE
    
    for code in all_codes:
        df1 = df[df['ts_code'] == code][['trade_date', 'close']].sort_values('trade_date', ascending=True)
        if df1.shape[0] > 0:
            df1['ave_close%s' % N] = get_ave_line(df1['close'], N)
            df1['close'] = df1['close'].apply(pd.to_numeric)
            if df1['ave_close%s' % N].iat[-1] * (1 - M) < df1['close'].iat[-1] < df1['ave_close%s' % N].iat[-1] * (1 + M) :
                result[0].append(code)
    
    print('%s日均线附近 %s%% 的合约：' % (N, M * 100))
    print(result[0])
            
    for codes in CODE_COMBINATION:
        code1 = codes[0]
        code2 = codes[1]
        df1 = add_close_difference(df, code1, code2)
        if df1.shape[0] > 0:
            df1['ave_close%s' % N] = get_ave_line(df1['difference'], N)
            if df1['ave_close%s' % N].iat[-1] * (1 - M) < df1['difference'].iat[-1] < df1['ave_close%s' % N].iat[-1] * (1 + M) :
                result[1].append(codes)
            if df1['ave_close%s' % N].iat[-1] - D < df1['difference'].iat[-1] < df1['ave_close%s' % N].iat[-1] + D :
                result[2].append(codes)
    
    print('%s日均线附近 %s%% 的一一合约组合：' % (N, M * 100))
    print(result[1])
    print('%s日均线附近 %s 的一一合约组合：' % (N, D))
    print(result[2])
                
    for codes in CODE_COMBINATION2:
        code1 = codes[0]
        code2 = codes[1]
        df1 = add_close_difference(df, code1, code2 , 2)
        if df1.shape[0] > 0:
            df1['ave_close%s' % N] = get_ave_line(df1['difference'], N)
            if df1['ave_close%s' % N].iat[-1] * (1 - M) < df1['difference'].iat[-1] < df1['ave_close%s' % N].iat[-1] * (1 + M) :
                result[3].append(codes)
            if df1['ave_close%s' % N].iat[-1] - D < df1['difference'].iat[-1] < df1['ave_close%s' % N].iat[-1] + D :
                result[4].append(codes)
    
    print('%s日均线附近 %s%% 的一二合约组合：' % (N, M * 100))
    print(result[3])
    print('%s日均线附近 %s 的一二合约组合：' % (N, D))
    print(result[4])
    return result


def get_code_near_ave2(df, N1, N2, N3, M):
    """
    获取多个N日均线同一侧的合约
    N:均线日期
    M:均线邻近区间比率
    """
    result = []
    all_codes = ZCE_CODE + DCE_CODE + SHF_CODE
    for code in all_codes:
        df1 = df[df['ts_code'] == code][['trade_date', 'close']].sort_values('trade_date', ascending=True)
        if df1.shape[0] > 0:
            df1['ave_close%s' % N1] = get_ave_line(df1['close'], N1)
            df1['ave_close%s' % N2] = get_ave_line(df1['close'], N2)
            df1['ave_close%s' % N3] = get_ave_line(df1['close'], N3)
            df1['close'] = df1['close'].apply(pd.to_numeric)
            if max(df1['ave_close%s' % N1].iat[-1], df1['ave_close%s' % N2].iat[-1], df1['ave_close%s' % N3].iat[-1]) < df1['close'].iat[-1] < max(df1['ave_close%s' % N1].iat[-1], df1['ave_close%s' % N2].iat[-1], df1['ave_close%s' % N3].iat[-1]) * (1 + M) or min(df1['ave_close%s' % N1].iat[-1], df1['ave_close%s' % N2].iat[-1], df1['ave_close%s' % N3].iat[-1]) * (1 - M) < df1['close'].iat[-1] < min(df1['ave_close%s' % N1].iat[-1], df1['ave_close%s' % N2].iat[-1], df1['ave_close%s' % N3].iat[-1]):
                result.append(code)
    
    print('%s,%s,%s日均线附近 %s%% 的合约：' % (N1, N2, N3, M * 100))
    print(result)


def get_code_fit_strategy(df):
    """
    获取符合N和NM策略的合约
    """
    result_N = []
    result_NM = [[], []]
    for x in BEST_N:
        code = x[0]
        N = x[1]
        df_code = df[df['ts_code'] == code][['trade_date', 'close', 'year']].sort_values('trade_date', ascending=True)
        df_code['ave_close%s' % N] = get_ave_line(df_code['close'], N)
        df_code['difference'] = df_code['close'] - df_code['ave_close%s' % N]
        if df_code[-1:]['difference'].values[0] * df_code[-2:-1]['difference'].values[0] <= 0:
            result_N.append(code)
    
    print('符合N策略的合约：')
    print(result_N)
    
    for x in BEST_NM:
        code = x[0]
        N = x[1]
        M = x[2]
        trade_trend = '平'
        
        df_code = df[df['ts_code'] == code][['trade_date', 'close', 'year']].sort_values('trade_date', ascending=True)
        year = df_code[-1:]['year'].values[0]
        df_year = df_code[df_code['year'] == year][15:]
        
        i = N
        if df_year.shape[0] > N:
            while(i < df_year.shape[0] - 1):
                if trade_trend == '平' :
                    if df_year[i:i + 1]['close'].values[0] > df_year[i - N : i]['close'].max():
                        trade_trend = '多'
                    elif df_year[i:i + 1]['close'].values[0] < df_year[i - N : i]['close'].min():
                        trade_trend = '空'
                    else:
                        pass
                elif trade_trend == '多' :
                    if df_year[i:i + 1]['close'].values[0] < df_year[i - M : i]['close'].min():
                        trade_trend = '平'
                    else:
                        pass
                elif trade_trend == '空':
                    if df_year[i:i + 1]['close'].values[0] > df_year[i - M : i]['close'].max():
                        trade_trend = '平'
                    else:
                        pass
                else:
                    pass
                i = i + 1
            if trade_trend == '平':
                if df_year[-1:]['close'].values[0] > df_year[-1 - N :-1]['close'].max() or df_year[-1:]['close'].values[0] < df_year[-1 - N :-1]['close'].min():
                    result_NM[0].append('%s-%s-%s' % (code, N, M))
            else:
                if df_year[-1:]['close'].values[0] < df_year[-1 - M :-1]['close'].min() or df_year[-1:]['close'].values[0] > df_year[-1 - M :-1]['close'].max():
                    result_NM[1].append('%s-%s-%s' % (code, N, M))

    print('符合NM策略入场的合约：')
    print(result_NM[0])
    print('符合NM策略离场的合约：')
    print(result_NM[1])
    return result_N, result_NM
    

def show1(df, code, N):
    """
    展示单份合约收盘价与N日均线
    """
    df1 = df[df['ts_code'] == code][['trade_date', 'close', 'vol', 'oi']].sort_values('trade_date', ascending=True)
    df1['trade_date'] = df1['trade_date'].apply(lambda x: datetime.datetime.strptime(str(x), '%Y%m%d'))
    df1['ave_close%s' % N] = get_ave_line(df1['close'], N)
    plt.plot(df1['trade_date'], df1['close'], c='red', label='close')
    plt.plot(df1['trade_date'], df1['ave_close%s' % N], c='blue', label='ave_close%s' % N)
    plt.legend(loc='upper left')
    plt.suptitle('%s (N=%s)' % (code, N))
    plt.show()


def show2(df, code1, code2, N):
    """
    展示两份合约成交量、持仓量、差价及N日差价
    """
    result = add_close_difference(df, code1, code2)
    result['trade_date'] = result['trade_date'].apply(lambda x: datetime.datetime.strptime(str(x), '%Y%m%d'))
    result['ave_difference%s' % N] = get_ave_line(result['difference'], N)
    result['ave_close1%s' % N] = get_ave_line(result['close1'], N)
    result['ave_close2%s' % N] = get_ave_line(result['close2'], N)
#     plt.figure(1)
#     plt.subplot(311)
#     plt.plot(result['trade_date'], result['difference'], c='red', label='difference')
#     plt.plot(result['trade_date'], result['ave_difference%s' % N], c='blue', label='ave_difference%s' % N)
#     plt.legend(loc='upper left')
#     plt.subplot(312)
#     plt.plot(result['trade_date'], result['oi1'], c='red', label='oi1')
#     plt.plot(result['trade_date'], result['oi2'], c='blue', label='oi2')
#     plt.legend(loc='upper left')
#     plt.subplot(313)
#     plt.plot(result['trade_date'], result['vol1'], c='red', label='vol1')
#     plt.plot(result['trade_date'], result['vol2'], c='blue', label='vol2')
#     plt.legend(loc='upper left')
#     plt.suptitle('%s and %s (N=%s)' % (code1, code2, N))
#     plt.show()
    return result['trade_date'].tolist(), result['difference'].tolist(), result['ave_difference%s' % N].tolist(), result['oi1'].tolist(), result['oi2'].tolist(), result['vol1'].tolist(), result['vol2'].tolist()


if __name__ == '__main__':
    
    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    
    strat_date = 20150101
    end_date = 20181231
    df_source = df_source[df_source['trade_date'] > strat_date]
    
    N = 60
    M = 0.01
    D = 20
    
#     result_codes = get_code_near_ave(df_source, N, M , D)

    get_code_fit_strategy(df_source)
#     result_codes = DCE_CODE
#     for code in result_codes:
#         if isinstance(code, str):
#             show1(df_source, code, N)
#         else:
#             show2(df_source, code[0], code[1], N)

#     show1(df_source, 'CF 01', N)
#     show2(df_source, 'C 01', 'C 05', N)
    
