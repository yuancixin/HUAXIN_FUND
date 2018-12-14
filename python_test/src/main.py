# coding=UTF-8
'''
Created on 2018年12月8日

@author: wanglx
'''
import pandas as pd
import csv
from config.properties import SOURCE_DIR
import fetch_data.get_future_data
# import fetch_data.get_stock_data
import fetch_data.get_actual_price
import trading_strategy.future_strategy_NM


def update_date():
    fetch_data.get_future_data.main()
#     fetch_data.get_stock_data.main()
    fetch_data.get_actual_price.main()


if __name__ == '__main__':    
    
    update_date()
    N = 26
    M = 0.01
    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    trading_strategy.future_strategy_NM.get_code_near_ave(df_source, N, M)
    trading_strategy.future_strategy_NM.get_code_fit_strategy(df_source)
    
