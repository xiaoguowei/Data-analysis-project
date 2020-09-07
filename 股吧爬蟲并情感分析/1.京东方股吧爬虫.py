import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import pymysql
#設定數據庫
conn=pymysql.connect(host='localhost',port=3306,database='xiaoguoweitest',user='root',password='a7788520')
cur=conn.cursor()
cur.execute('USE scraping')

#解析網址
headers = {'user-agent': '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
url='http://guba.eastmoney.com/list,000725_1.html'
res=requests.get(url,headers=headers)
res.encoding="utf-8"
print(res)#200表示成功獲取網址
soup=BeautifulSoup(res.text,'html.parser')

#閱讀量
yuedu=soup.find_all('span',class_='l1 a1')
yue_du=[]
#評論數
pinglun=soup.find_all('span',class_='l2 a2')
ping_lun=[]
#標題
biaoti=soup.find_all('span',class_='l3 a3')
biao_ti=[]
#作者
zuozhe=soup.find_all('span',class_='l4 a4')
zuo_zhe=[]
#時間
time=soup.find_all('span',class_='l5 a5')
ti_me=[]
for i in range(len(yuedu)-1):
    yue_du=(yuedu[1:][i].get_text())
    ping_lun=(pinglun[1:][i].get_text())
    biao_ti=(biaoti[1:][i].get_text())
    zuo_zhe=(zuozhe[1:][i].get_text())
    ti_me=(time[1:][i].get_text())
    sql = 'INSERT INTO guba(yuedu,pinglun,biaoti,zuozhe,gengxin_shijian) values(%s, %s, %s,%s,%s)'
    cur.execute(sql, (yue_du,ping_lun,biao_ti,zuo_zhe,ti_me))
    conn.commit()

conn.close()



