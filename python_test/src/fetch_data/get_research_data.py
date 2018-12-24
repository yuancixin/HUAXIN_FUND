# coding=UTF-8
'''
Created on 2018年12月24日

@author: wanglx
'''
import re
import json
import urllib.request
from bs4 import BeautifulSoup
from config.properties import RESEARCH_DIR


def save(filename, contents): 
    fh = open(filename, 'w') 
    fh.write(contents) 
    fh.close() 


def main():
    """
    下载东方财富网研报文件
    """
    print('---下载东方财富网研报数据---')
    res = urllib.request.urlopen("http://data.eastmoney.com/report/")
    html = res.read().decode("gb2312", "ignore")
    soup = BeautifulSoup(html, "html.parser")
    pattern = re.compile(r"var data =(.*?);", re.MULTILINE | re.DOTALL)
    script = soup.find("script", text=pattern)
    json_data = pattern.search(script.text).group(1)
#     print(json_data)
    hjson = json.loads(json_data)
    for x in hjson['data']:
        secuName = x['secuName']
        title = x['title']
        date = x['datetime'].split('T')[0].replace('-', '')
        infoCode = x['infoCode']
        print('正在下载%s-%s-%s' % (date, secuName, title))
        res = urllib.request.urlopen("http://data.eastmoney.com/report/%s/%s.html" % (date, infoCode))
        html = res.read().decode("gb2312", "ignore")
        soup = BeautifulSoup(html, "html.parser")
        link = soup.find_all('a', href=re.compile('pdf'))
        if len(link) > 0:
            urllib.request.urlretrieve(link[0]['href'], '%s/%s-%s-%s.pdf' % (RESEARCH_DIR, date, secuName, title))
        else:
            save('%s/%s-%s-%s.html' % (RESEARCH_DIR, date, secuName, title), soup.find('div', class_='newsContent').__str__()) 
    print('---下载完成---')


if __name__ == '__main__':
    main()
