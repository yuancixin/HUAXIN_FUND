'''
Created on 2018年12月7日

@author: wanglx
'''
import pandas as pd
import csv
from config.properties import RESULT_DIR
from config.properties import ZCE_CODE, DCE_CODE, SHF_CODE

if __name__ == '__main__':
    df_source = pd.read_csv('%s/NM_BREAKTHROUGH_RESULT.csv' % RESULT_DIR, quoting=csv.QUOTE_NONE)
    
#     codes = ZCE_CODE + DCE_CODE + SHF_CODE
    codes = ZCE_CODE
    for code in codes:
        df = df_source[df_source['ts_code'] == code]
        df = df.sort_values('capital_available', ascending=False)
        df.drop('Unnamed: 0', axis=1, inplace=True)
        df.to_csv('%s/NM/%s.csv' % (RESULT_DIR, code), index=0, encoding='utf-8')
