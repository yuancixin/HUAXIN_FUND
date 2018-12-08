# coding=UTF-8
'''
Created on 2018年12月3日

@author: wanglx
'''
import pandas as pd
import numpy as np
import csv
import os
from config.properties import SOURCE_DIR, RESULT_DIR
from config.properties import DCE_CODE, SHF_CODE


def get_ave_line(column, N):
    """
    返回数据列的均线
    输入为DataFrame的某一列，均线日期
    """
    return np.round(pd.Series.rolling(column, window=N).mean(), 2)


def backtest1(df, code, N):
    """
    N策略交易结果
    """   
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
        nonlocal capital_available, hold_num, B_PRICE, S_PRICE, trade_num , capital_last, retreat_max , capital_max, capital_min, profit_num
        capital_available = hold_num * (S - B) * 10 + capital_available
        
        if capital_available > capital_max:
            capital_max = capital_available
        if capital_available < capital_min:
            capital_min = capital_available
        
        retreat = (capital_available - capital_last) / capital_last * 100
        
        if retreat > 0 :
            profit_num = profit_num + 1
        if retreat < retreat_max:
            retreat_max = retreat
        capital_last = capital_available
        print('平仓，当前总资产%s，S--%s,B--%s' % (capital_available, S, B))
        hold_num = 0
        B_PRICE = 0
        S_PRICE = 0
        trade_num = trade_num + 1
    
    capital_base = 1000000  # 初始资本
    capital_available = 1000000  # 可用资金
    capital_last = 1000000  # 上次资产
    retreat_max = 0  # 最大回撤率
    profit_num = 0  # 盈利次数
    
    capital_max = 1000000
    capital_min = 1000000
    
    B_PRICE = 0
    S_PRICE = 0
    trade_trend = '平'
    hold_num = 0
    trade_num = 0
    
    df_code = df[df['ts_code'] == code][['trade_date', 'close', 'year']].sort_values('trade_date', ascending=True)
    df_code['ave_close%s' % N] = get_ave_line(df_code['close'], N)
    df_code['difference'] = df_code['close'] - df_code['ave_close%s' % N]
    
    year_list = df_code['year'].drop_duplicates()
    for year in year_list:
        df_year = df_code[df_code['year'] == year][15:-15]
        i = 1
        while(i < df_year.shape[0] - 1):
            if df_year[i - 1:i]['difference'].values[0] * df_year[i:i + 1]['difference'].values[0] <= 0:
                print('======%s触发交易======' % df_year[i:i + 1]['trade_date'].values[0])
#                 击穿
                if trade_trend == '平':
                    if df_year[i:i + 1]['difference'].values[0] > df_year[i - 1:i]['difference'].values[0]:  # 多
                        buy(df_year[i:i + 1]['close'].values[0])
                        trade_trend = '多'
                    elif df_year[i:i + 1]['difference'].values[0] < df_year[i - 1:i]['difference'].values[0]:  # 空
                        sell(df_year[i:i + 1]['close'].values[0])
                        trade_trend = '空'
                
                elif trade_trend == '多':
                    unwind(df_year[i:i + 1]['close'].values[0] , B_PRICE)
                    trade_trend = '空'
                    sell(df_year[i:i + 1]['close'].values[0])
                    
                elif trade_trend == '空':
                    unwind(S_PRICE , df_year[i:i + 1]['close'].values[0])
                    trade_trend = '多'
                    buy(df_year[i:i + 1]['close'].values[0])              
            else:
                pass
                        
            i = i + 1 
        
        if trade_trend == '多':
            print('======%s因合约结束，平仓======' % df_year[i:i + 1]['trade_date'].values[0])
            unwind(df_year[i:i + 1]['close'].values[0] , B_PRICE)
            trade_trend = '平'
        elif trade_trend == '空':
            print('======%s因合约结束，平仓======' % df_year[i:i + 1]['trade_date'].values[0])
            unwind(S_PRICE , df_year[i:i + 1]['close'].values[0])
            trade_trend = '平'
        else:
            pass
    
    print('N为%s--交易次数%s--盈利次数%s--单次最大回撤%s--最大资产%s--最小资产%s--最终资产%s' % (N, trade_num, profit_num, round(retreat_max, 2), round(capital_max, 2), round(capital_min, 2), round(capital_available, 2)))
    return [code, N, trade_num, profit_num, round(retreat_max, 2), round(capital_available, 2), round(capital_max, 2), round(capital_min, 2)]


if __name__ == '__main__':
    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    
    backtest1(df_source, 'RB 05',96 )
    
#     codes = SHF_CODE + DCE_CODE
#     for code in codes:
#         result_list = []
#         for N in range(5, 201, 1):
#             result_list.append(backtest1(df_source, code, N))
#         df_result = pd.DataFrame(result_list, columns=('ts_code', 'N', 'trade_num', 'profit_num', 'retreat_max', 'capital_available', 'capital_max', 'capital_min'))  # 生成空的pandas表
#         df_result.to_csv('%s/N_AVERAGE_RESULT.csv' % RESULT_DIR, header=not os.path.exists('%s/N_AVERAGE_RESULT.csv' % RESULT_DIR), mode='a', encoding='utf-8')       

