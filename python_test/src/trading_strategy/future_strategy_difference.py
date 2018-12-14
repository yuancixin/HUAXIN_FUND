# coding=UTF-8
'''
Created on 2018年12月14日

@author: wanglx
'''

import pandas as pd
import csv
from config.properties import SOURCE_DIR


def get_difference(df, code):
    
    df_future = df[df['ts_code'] == code][['trade_date', 'close']].sort_values('trade_date', ascending=True)
    df_actual = pd.read_csv('%s/%s_price.csv' % (SOURCE_DIR, code.split(' ')[0]), quoting=csv.QUOTE_NONE)
    df_actual = df_actual[['trade_date', 'ave_price']]
    df_difference = pd.merge(df_actual, df_future, how='left')
    df_difference['ave_price'] = df_difference['ave_price'] * 1000
    print(df_difference)
    

if __name__ == '__main__':
    
    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    code = 'JD 03'
    get_difference(df_source, code)
