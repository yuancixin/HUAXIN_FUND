'''
Created on 2018年11月26日

@author: wanglx
'''
# coding=UTF-8
import pandas as pd
import numpy as np
import csv
from config.properties import SOURCE_DIR
import matplotlib.pyplot as plt


def strategy(code1, code2):

    df1 = df[df['ts_code'] == code1][['trade_date', 'close', 'vol', 'oi']].sort_values('trade_date', ascending=True)
    df2 = df[df['ts_code'] == code2][['trade_date', 'close', 'vol', 'oi']].sort_values('trade_date', ascending=True)
    
    df1.columns = ['trade_date', 'close1', 'vol1', 'oi1' ]
    df2.columns = ['trade_date', 'close2', 'vol2', 'oi2' ]
    
    result = pd.merge(df1, df2, on='trade_date', how='inner')
    result[['close1', 'close2', 'vol1', 'vol2', 'oi1', 'oi2']] = result[['close1', 'close2', 'vol1', 'vol2', 'oi1', 'oi2']].apply(pd.to_numeric)
    
    result['difference'] = result['close1'] - result['close2']
#     result['ave_difference'] = np.round(pd.Series.rolling(result['difference'], window=20).mean(), 2)
    return result 


def get_ave_difference(result, day):
    return np.round(pd.Series.rolling(result['difference'], window=day).mean(), 2)

def show(code1,code2,day):
    result = strategy(code1, code2)
    result['ave_difference%s' % day] = get_ave_difference(result, day)
    fig = plt.figure(1)
    plt.subplot(311)
    plt.plot(result['trade_date'], result['difference'], c='red', label='difference')
    plt.plot(result['trade_date'], result['ave_difference%s' % day], c='blue', label='ave_difference%s' % day)
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

if __name__ == '__main__':
    
    df = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    code1 = 'C 01'
    code2 = 'C 05'
    day = 60
    show(code1,code2,day)
#     print(result)
    
