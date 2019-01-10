# coding=UTF-8
'''
Created on 2018年12月14日

@author: wanglx
'''

import pandas as pd
import csv
import datetime
import matplotlib.pyplot as plt
from config.properties import SOURCE_DIR


def get_difference(df, code):
    
    df_future = df[df['ts_code'] == code][['trade_date', 'close']].sort_values('trade_date', ascending=True)
    print(df_future)
    df_actual = pd.read_csv('%s/%s_price.csv' % (SOURCE_DIR, code.split(' ')[0]), quoting=csv.QUOTE_NONE)
    print(df_actual)
    df_actual = df_actual[['trade_date', 'ave_price']]
    df_difference = pd.merge(df_actual, df_future, how='left')
    df_difference.sort_values('trade_date', ascending=True)
    df_difference['ave_price'] = df_difference['ave_price'] * 1000
    df_difference['trade_date'] = df_difference['trade_date'].apply(lambda x: datetime.datetime.strptime(str(x), '%Y%m%d'))
    df_difference['difference'] = df_difference['ave_price'] - df_difference['close']
#     print(df_difference)
#     plt.plot(df_difference['trade_date'], df_difference['difference'], c='red', label='difference')
#     plt.show()
    return df_difference['trade_date'].tolist(), df_difference['difference'].tolist()
    

if __name__ == '__main__':
    
    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    code = 'JD 03'
    x, y = get_difference(df_source, code)
    print(x)
    print(y)
