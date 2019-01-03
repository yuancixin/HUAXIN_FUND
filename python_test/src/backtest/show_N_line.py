# coding=UTF-8
'''
Created on 2018年12月6日

@author: wanglx
'''
import pandas as pd
import csv
from config.properties import RESULT_DIR
from config.properties import ZCE_CODE, DCE_CODE, SHF_CODE
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df_source = pd.read_csv('%s/N_AVERAGE_RESULT.csv' % RESULT_DIR, quoting=csv.QUOTE_NONE)
    
    codes = ['J 01']
#     codes = ZCE_CODE + DCE_CODE + SHF_CODE
    for code in codes:
        df = df_source[df_source['ts_code'] == code]
        plt.subplot(511)
        plt.plot(df['N'], df['capital_available'], c='red', label='capital_available')
        plt.legend(loc='upper left')
        plt.subplot(512)
        plt.plot(df['N'], df['capital_max'], c='blue', label='capital_max')
        plt.legend(loc='upper left')
        plt.subplot(513)
        plt.plot(df['N'], df['capital_min'], c='green', label='capital_min')
        plt.legend(loc='upper left')
        plt.subplot(514)
        plt.plot(df['N'], round(df['profit_num'] / df['trade_num'], 2), c='green', label='win')
        plt.legend(loc='upper left')
        plt.subplot(515)
        plt.plot(df['N'], df['retreat_max'], c='green', label='retreat_max')
        plt.legend(loc='upper left')
        plt.suptitle('code = %s' % code)
        plt.show()
