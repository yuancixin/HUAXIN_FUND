# coding=UTF-8

import os
import cx_Oracle as Oracle
import pandas as pd
import numpy as np
import math
import random
import csv

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

if __name__ == '__main__':
    # connect oracle database
    db = Oracle.connect('qyhxcpk/Qyhxcpk_11@172.22.5.61:1526/dcappdb')

    # create cursor
    cursor = db.cursor()
    
    file = open('G:/xxx.csv')
    while True:
        line = file.readline()
        if not line:
            break
        cursor.execute('SELECT count(*) FROM %s' %line)
        data = cursor.fetchall()
        print('%s,%s' %(line,data)) 
    file.close() 
    cursor.close()
    db.close()