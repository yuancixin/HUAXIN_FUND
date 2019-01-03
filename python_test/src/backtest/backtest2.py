# coding=UTF-8
'''
Created on 2018年12月3日

@author: wanglx
'''
import pandas as pd
import csv
import os
from config.properties import SOURCE_DIR, RESULT_DIR
from config.properties import ZCE_CODE, DCE_CODE, SHF_CODE


def backtest(df, code, N, M):
    """
    NM策略结果
    """
#     capital_base = 1000000  # 初始资本
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
    
    def buy(price):
        nonlocal B_PRICE, hold_num
        B_PRICE = price
        hold_num = capital_available / B_PRICE
#         print('以%s买入' % price)

    def sell(price):
        nonlocal S_PRICE, hold_num
        S_PRICE = price
        hold_num = capital_available / S_PRICE
#         print('以%s卖出' % price)
        
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
#         print('当前总资产%s，S--%s,B--%s' % (capital_available, S, B))
        hold_num = 0
        B_PRICE = 0
        S_PRICE = 0
        trade_num = trade_num + 1
    
    df_code = df[df['ts_code'] == code][['trade_date', 'close', 'year']].sort_values('trade_date', ascending=True)
    
    year_list = df_code['year'].drop_duplicates()
    for year in year_list:
        df_year = df_code[df_code['year'] == year][15:-15]
        i = N
        if df_year.shape[0] > N:
            while(i < df_year.shape[0] - 1):
                if trade_trend == '平' :
                    if df_year[i:i + 1]['close'].values[0] > df_year[i - N : i]['close'].max():
#                         print('======%s做多======' % df_year[i:i + 1]['trade_date'].values[0])
                        buy(df_year[i:i + 1]['close'].values[0])
                        trade_trend = '多'
                    elif df_year[i:i + 1]['close'].values[0] < df_year[i - N : i]['close'].min():
#                         print('======%s做空======' % df_year[i:i + 1]['trade_date'].values[0])
                        sell(df_year[i:i + 1]['close'].values[0])
                        trade_trend = '空'
                    else:
                        pass
                elif trade_trend == '多' :
                    if df_year[i:i + 1]['close'].values[0] < df_year[i - M : i]['close'].min():
#                         print('======%s平仓======' % df_year[i:i + 1]['trade_date'].values[0])
                        unwind(df_year[i:i + 1]['close'].values[0] , B_PRICE)
                        trade_trend = '平'
                    else:
                        pass
                elif trade_trend == '空':
                    if df_year[i:i + 1]['close'].values[0] > df_year[i - M : i]['close'].max():
#                         print('======%s平仓======' % df_year[i:i + 1]['trade_date'].values[0])
                        unwind(S_PRICE , df_year[i:i + 1]['close'].values[0])
                        trade_trend = '平'
                    else:
                        pass
                else:
                    pass
                
                i = i + 1
                
            if trade_trend == '多':
#                 print('======%s因合约结束，平仓======' % df_year[i:i + 1]['trade_date'].values[0])
                unwind(df_year[i:i + 1]['close'].values[0] , B_PRICE)
                trade_trend = '平'
            elif trade_trend == '空':
#                 print('======%s因合约结束，平仓======' % df_year[i:i + 1]['trade_date'].values[0])
                unwind(S_PRICE , df_year[i:i + 1]['close'].values[0])
                trade_trend = '平'
            else:
                pass

    print('N为%s--M为%s--交易次数%s--盈利次数%s--单次最大回撤%s--最大资产%s--最小资产%s--最终资产%s' % (N, M, trade_num, profit_num, round(retreat_max, 2), round(capital_max, 2), round(capital_min, 2), round(capital_available, 2)))
    return [code, N, M, trade_num, profit_num, round(retreat_max, 2), round(capital_available, 2), round(capital_max, 2), round(capital_min, 2)]


if __name__ == '__main__':
    
    df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    
#     backtest(df_source, 'RM 11', 11, 11)
    
#     codes = ZCE_CODE + SHF_CODE + DCE_CODE
    codes = [
             'AL 03', 'SR 05', 'ZC 09', 'MA 01', 'FG 05', 'NI 07', 'SN 01', 
             'AL 12', 'ZN 01', 'CU 02', 'MA 09', 'OI 09', 'ZN 07', 'ZN 10', 'SC 01', 'SP 09', 'AP 07', 'BU 09', 'SC 07', 'BU 06', 
             'AU 12', 'CU 11', 'Y 09', 'TA 09', 'RM 09', 'AP 10', 'SM 01', 'NI 12', 'SC 05', 'OI 05', 'OI 01', 'AP 05', 'AU 06', 
             'SF 05', 'FU 05', 'SF 01', 'EG 01', 'SF 09', 'ZN 06', 'AG 12', 'ZN 04', 'CU 04', 'SC 11', 'NI 09', 'SN 09', 'AP 02', 
             'AL 05', 'ZN 05', 'WH 01', 'CU 10', 'TA 03', 'CU 08', 'SR 09', 'ZN 08', 'PB 06', 'SC 08', 'SM 09', 'PB 04', 'TA 05']
    for code in codes:
        result_list = []
        for N in range(10, 101, 1):
            for M in range(1, N + 1, 1):
                result_list.append(backtest(df_source, code, N, M))
        df_result = pd.DataFrame(result_list, columns=('ts_code', 'N', 'M', 'trade_num', 'profit_num', 'retreat_max', 'capital_available', 'capital_max', 'capital_min'))  # 生成空的pandas表
        df_result.to_csv('%s/NM_BREAKTHROUGH_RESULT.csv' % RESULT_DIR, header=not os.path.exists('%s/NM_BREAKTHROUGH_RESULT.csv' % RESULT_DIR), mode='a', index=0, encoding='utf-8')
            
