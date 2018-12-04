# coding=UTF-8
'''
Created on 2018年12月3日

@author: wanglx
'''
import pandas as pd
import numpy as np
import csv
from config.properties import SOURCE_DIR


def get_ave_line(column, N):
    """
    返回数据列的均线
    输入为DataFrame的某一列，均线日期
    """
    return np.round(pd.Series.rolling(column, window=N).mean(), 2)


def backtest1(df, code, N):
    
    def buy(price):
        nonlocal B_PRICE, hold_num
        B_PRICE = price
        hold_num = capital_available / B_PRICE
        print('以%s买入' % price)

    def sell(price):
        nonlocal S_PRICE, hold_num
        S_PRICE = price
        hold_num = capital_available / S_PRICE
        print('以%s卖出' % price)
        
    def unwind(S, B):
        nonlocal capital_available, hold_num, B_PRICE, S_PRICE
        capital_available = hold_num * (S - B) * 10 + capital_available
        print('平仓，当前总资产%s，S--%s,B--%s' % (capital_available, S, B))
        hold_num = 0
        B_PRICE = 0
        S_PRICE = 0
    
    capital_base = 1000000  # 初始资本
    capital_available = 1000000  # 可用资金
    
    hold_num = 0
    trade_trend = '平'
    B_PRICE = 0
    S_PRICE = 0
    
    df_code = df[df['ts_code'] == code][['trade_date', 'close', 'year']].sort_values('trade_date', ascending=True)
    df_code['ave_close%s' % N] = get_ave_line(df_code['close'], N)
    df_code['difference'] = df_code['close'] - df_code['ave_close%s' % N]
    
    year_list = df_code['year'].drop_duplicates()
    for year in year_list:
        df_year = df_code[df_code['year'] == year]
        i = 1
        while(i < df_year.shape[0] - 1):
            if df_year[i - 1:i]['difference'].values[0] * df_year[i:i + 1]['difference'].values[0] <= 0:
#                 击穿
                if trade_trend == '平':
                    if df_year[i:i + 1]['difference'].values[0] > df_year[i - 1:i]['difference'].values[0]:  # 多
                        buy(df_year[i:i + 1]['close'].values[0])
#                         print('%s以%s买入' % (df_year[i:i + 1]['trade_date'].values[0], df_year[i:i + 1]['close'].values[0]))
                        trade_trend = '多'
                    elif df_year[i:i + 1]['difference'].values[0] < df_year[i - 1:i]['difference'].values[0]:  # 空
                        sell(df_year[i:i + 1]['close'].values[0])
#                         print('%s以%s卖出' % (df_year[i:i + 1]['trade_date'].values[0], df_year[i:i + 1]['close'].values[0]))
                        trade_trend = '空'
                
                elif trade_trend == '多':
                    unwind(df_year[i:i + 1]['close'].values[0] , B_PRICE)
#                     print('%s以%s平仓' %(df_year[i:i + 1]['trade_date'].values[0], df_year[i:i + 1]['close'].values[0]))
                    trade_trend = '空'
                    sell(df_year[i:i + 1]['close'].values[0])
#                     print('%s以%s卖出' % (df_year[i:i + 1]['trade_date'].values[0], df_year[i:i + 1]['close'].values[0]))
                    
                elif trade_trend == '空':
                    unwind(S_PRICE , df_year[i:i + 1]['close'].values[0])
#                     print('%s以%s平仓' %(df_year[i:i + 1]['trade_date'].values[0], df_year[i:i + 1]['close'].values[0]))
                    trade_trend = '多'
                    buy(df_year[i:i + 1]['close'].values[0])
#                     print('%s以%s买入' % (df_year[i:i + 1]['trade_date'].values[0], df_year[i:i + 1]['close'].values[0]))
                    
            else:
                pass
                        
            i = i + 1 
        
        if trade_trend == '多':
            print('合约结束，平仓')
            unwind(df_year[i:i + 1]['close'].values[0] , B_PRICE)
        elif trade_trend == '空':
            print('合约结束，平仓')
            unwind(S_PRICE , df_year[i:i + 1]['close'].values[0])
        else:
            pass
            
    print('最终资产%s' % capital_available)

#         print(df_year)


if __name__ == '__main__':
    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    
    N = 60
    code = 'JD 05'
    backtest1(df_source, code, N)
