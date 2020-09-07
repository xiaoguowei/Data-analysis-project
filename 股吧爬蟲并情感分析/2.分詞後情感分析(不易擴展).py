import jieba
from snownlp import SnowNLP
import pymysql
#設定數據庫
conn=pymysql.connect(host='localhost',port=3306,database='xiaoguoweitest',user='root',password='a7788520')
cur=conn.cursor()
cur.execute('USE scraping')
#匯入負面情緒字典
fumian = open('fumian.txt','r',encoding='utf-8')
negitive= fumian.readlines()
negi_tive= []
for arr in negitive:
    arr = arr.replace("\n", "")  # 把換行替換成空白
    negi_tive.append(arr)

#匯入正面情緒詞典
zhengmian = open('zhengmian.txt','r',encoding='utf-8')
posstive= zhengmian.readlines()
poss_tive = []
for arr in posstive:
    arr = arr.replace("\n", "")  # 把換行替換成空白
    poss_tive.append(arr)

#匯入停用詞
tingyong = open('stop.txt','r',encoding='utf-8')
stopwords = tingyong.readlines()
arr = []
for stopword in stopwords:
    stopword = stopword.replace("\n", "")  # 把換行替換成空白
    arr.append(stopword)

fumian=[]
zhengmian=[]
with open('biaoti.txt', 'r', encoding='UTF-8') as f: #打開要分詞的標題
    score=[]
    for sentence in f.readlines():
        s = SnowNLP(sentence)
        s1 = SnowNLP(s.sentences[0])
        score.append(s1.sentiments)
        # 標題分詞
        seg_list = jieba.cut(sentence)
        seg_result = []
        for w in seg_list:
            seg_result.append(w)
        # 已分詞的標題去掉停用詞
        new_sent = []
        for word in seg_result:
            if word not in arr:
                new_sent.append(word)
        zhengmian = 0
        fumian = 0
        #計分
        for word in seg_result: #遍歷已分詞和去掉停用詞的標題
            if word in negi_tive:  # 如果在負面就+1
                zhengmian += 1
            elif word in poss_tive: # 如果在正面就+1
                fumian += 1

        final_score = zhengmian - fumian
        print("已分詞:",seg_result)
        print('正面情緒用詞:', zhengmian)
        print('負面情緒用詞:', fumian)
        print("情感值:", s1.sentiments)
        print("------------------------------------------")
print(score)
