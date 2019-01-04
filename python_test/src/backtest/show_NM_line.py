import pandas as pd
import csv
import matplotlib.pyplot as plt
from config.properties import RESULT_DIR


def show_nm(df, code, N):
    df_code = df[(df['ts_code'] == code) & (df['N'] == N)]
    plt.subplot(111)
    plt.plot(df_code['M'], df_code['capital_available'], c='red', label='capital_available')
    plt.plot(df_code['M'], df_code['capital_max'], c='blue', label='capital_max')
    plt.plot(df_code['M'], df_code['capital_min'], c='green', label='capital_min')
    plt.legend(loc='upper left')
    plt.suptitle('%s (N=%s)' % (code, N))
    plt.show()


if __name__ == '__main__':
    
    df_source = pd.read_csv('%s/NM_BREAKTHROUGH_RESULT.csv' % RESULT_DIR, quoting=csv.QUOTE_NONE)
    
    code = 'J 09'
    N = 40
    
    show_nm(df_source, code, N)
    
