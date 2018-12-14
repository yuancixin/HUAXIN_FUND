# coding=UTF-8
'''
Created on 2018年12月13日

@author: wanglx
'''
import pandas as pd
import csv
import os
import urllib.request
import datetime
from bs4 import BeautifulSoup
from config.properties import SOURCE_DIR


def main():
    """
    采集德州鸡蛋平均价格，网站每日10点前更新
    """
    print('---采集最新鸡蛋价格---')
    today = datetime.datetime.now().strftime('%Y%m%d')
    res = urllib.request.urlopen("http://www.zhujiage.com.cn/yangji/jidanjiage/")
    html = res.read().decode("gb2312", "ignore")
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all('a')

    herf = ''
    for link in links:
        if '山东鸡蛋价格行情' in link.get_text():
            herf = link['href']
#             print(link.name, link['href'], link.get_text())
            break

    res = urllib.request.urlopen(herf)
    html = res.read().decode("gb2312", "ignore")
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.get_text()
    p_list = soup.find('div', id='content').find_all('p')
    price_list = []
    for i in p_list:
        if '德州-' in i.get_text():
            price_list.append(float(i.get_text().split('参考价')[1]))
            
    price_sum = 0
    for i in price_list:
        price_sum = price_sum + i
        
    ave_price = price_sum / len(price_list)
    
    result = [[today, str(round(ave_price, 3)), ";".join([str(x) for x in price_list]), title]]
    df_result = pd.DataFrame(result, columns=('date', 'ave_price', 'price_list', 'title'))
    print(df_result[['title','ave_price']])
    df_result.to_csv('%s/egg_price.csv' % SOURCE_DIR, header=not os.path.exists('%s/egg_price.csv' % SOURCE_DIR), mode='a', index=0, encoding='utf-8')  
    print('---采集完成，正在进行数据清洗---')
    df_source = pd.read_csv('%s/egg_price.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
    df_source.sort_values(by=['title', 'date'], ascending=(True, True), inplace=True)
    df_source.drop_duplicates(subset=['title'], keep='first', inplace=True)
    df_source.to_csv('%s/egg_price.csv' % SOURCE_DIR, index=0, encoding='utf-8')
    print('---数据更新完成---')
    
    
if __name__ == '__main__':
    main()   
    
