# coding=UTF-8
'''
Created on 2018年12月12日

@author: wanglx
'''

import pandas as pd
import csv
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf
from config.properties import SOURCE_DIR


def show_seasonal_decompose(df, code, cycle):
    
    df_code = df[df['ts_code'] == code].sort_values('trade_date', ascending=True)
    if ADF(df_code['close'])[1] > 0.05:
        print('是非平稳')
        decomposition = seasonal_decompose(df_code['close'], model="additive", freq=cycle)
        decomposition.plot()
        plot_acf(df_code['close']).show()
        plt.show()
    else:
        print('平稳序列')
        decomposition = seasonal_decompose(df_code['close'], model="additive", freq=cycle)
        decomposition.plot()
        plot_acf(df_code['close']).show()
        plt.show()


if __name__ == '__main__': 
    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    code = 'M 05'
    cycle = 1000
    show_seasonal_decompose(df_source, code, cycle)

