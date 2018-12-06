# coding=UTF-8
'''
Created on 2018年12月6日

@author: wanglx
'''
import pandas as pd
import csv
from config.properties import RESULT_DIR
from config.properties import DCE_CODE, SHF_CODE
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df_source = pd.read_csv('%s/N_AVERAGE_RESULT.csv' % RESULT_DIR, quoting=csv.QUOTE_NONE)
    
    codes = SHF_CODE + DCE_CODE
    for code in codes:
        df = df_source[df_source['ts_code'] == code]
        plt.subplot(311)
        plt.plot(df['N'], df['capital_available'], c='red', label='capital_available')
        plt.legend(loc='upper left')
        plt.subplot(312)
        plt.plot(df['N'], df['capital_max'], c='blue', label='capital_max')
        plt.legend(loc='upper left')
        plt.subplot(313)
        plt.plot(df['N'], df['capital_min'], c='green', label='capital_min')
        plt.legend(loc='upper left')
        plt.suptitle('code = %s' % code)
        plt.show()
