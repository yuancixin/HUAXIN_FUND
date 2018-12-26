# coding=UTF-8
'''
Created on 2018年12月24日

@author: wanglx
'''
import re
import os
import json
import urllib.request
from bs4 import BeautifulSoup
from config.properties import RESEARCH_STOCK_DIR, RESEARCH_INDUSTRY_DIR


def save(filename, contents): 
    fh = open(filename, 'w') 
    fh.write(contents) 
    fh.close() 


def download_industry():
    """
    下载东方财富网行业研报文件
    """
    print('---下载东方财富网行业研报数据---')
    for page in range(1, 11):
        res = urllib.request.urlopen("http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=HYSR&mkt=0&stat=0&cmd=4&code=&sc=&ps=50&p=%s" % page)
        html = res.read().decode("utf_8", "ignore")[1:-1]
        json_string = json.loads(html)
        for x in json_string:
            x_split = x.split(',')
            secuName = x_split[10]
            title = x_split[9].replace('&sbquo;', '，').replace('&quot;', '').replace('/', '：').replace(':', '：')
            date = x_split[1].split(' ')[0].replace('/', '')
            infoCode = x_split[2]
            if os.path.exists('%s/%s-%s-%s.pdf' % (RESEARCH_INDUSTRY_DIR, date, secuName, title)) or os.path.exists('%s/%s-%s-%s.html' % (RESEARCH_INDUSTRY_DIR, date, secuName, title)):
                continue
            print('正在下载%s-%s-%s' % (date, secuName, title)) 
            res = urllib.request.urlopen("http://data.eastmoney.com/report/%s/hy,%s.html" % (date, infoCode))
            html = res.read().decode("gb2312", "ignore")
            soup = BeautifulSoup(html, "html.parser")
            link = soup.find_all('a', href=re.compile('pdf'))
            if len(link) > 0:
                urllib.request.urlretrieve(link[0]['href'], '%s/%s-%s-%s.pdf' % (RESEARCH_INDUSTRY_DIR, date, secuName, title))
            else:
                save('%s/%s-%s-%s.html' % (RESEARCH_INDUSTRY_DIR, date, secuName, title), soup.find('div', class_='newsContent').__str__()) 
    print('---下载完成---')
    

def download_stock():
    """
    下载东方财富网个股研报文件
    """
    print('---下载东方财富网个股研报数据---')
    for page in range(1, 11):
        res = urllib.request.urlopen("http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=GGSR&ps=50&p=%s&mkt=0&stat=0&cmd=2&code=" % page)
        html = res.read().decode("utf_8", "ignore")[1:-1]
        json_string = json.loads(html)
        for x in json_string:
            secuName = x['secuName']
            title = x['title'].replace('&sbquo;', '，').replace('&quot;', '').replace('/', '：').replace(':', '：')
            date = x['datetime'].split('T')[0].replace('-', '')
            infoCode = x['infoCode']
            if os.path.exists('%s/%s-%s-%s.pdf' % (RESEARCH_STOCK_DIR, date, secuName, title))  or os.path.exists('%s/%s-%s-%s.html' % (RESEARCH_STOCK_DIR, date, secuName, title)) :
                continue
            print('正在下载%s-%s-%s' % (date, secuName, title))
            res = urllib.request.urlopen("http://data.eastmoney.com/report/%s/%s.html" % (date, infoCode))
            html = res.read().decode("gb2312", "ignore")
            soup = BeautifulSoup(html, "html.parser")
            link = soup.find_all('a', href=re.compile('pdf'))
            if len(link) > 0:
                urllib.request.urlretrieve(link[0]['href'], '%s/%s-%s-%s.pdf' % (RESEARCH_STOCK_DIR, date, secuName, title))
            else:
                save('%s/%s-%s-%s.html' % (RESEARCH_STOCK_DIR, date, secuName, title), soup.find('div', class_='newsContent').__str__()) 
    print('---下载完成---')


def main():
    download_stock()
    download_industry()

    
if __name__ == '__main__':
    main()
