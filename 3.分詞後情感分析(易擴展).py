import jieba
#匯入負面情緒字典
fumian = open('fumian.txt','r',encoding='utf-8')
negitive= fumian.readlines()
negi_tive= []
for arr in negitive:
    arr = arr.replace("\n", "")#把換行替換成空白
    negi_tive.append(arr)

#匯入正面情緒詞典
zhengmian = open('zhengmian.txt','r',encoding='utf-8')
posstive= zhengmian.readlines()
poss_tive = []
for arr in posstive:
    arr = arr.replace("\n", "") #把換行替換成空白
    poss_tive.append(arr)

#標題分詞
def biaotifenci(sentence):
    seg_list = jieba.cut(sentence)
    seg_result = []
    for w in seg_list:
        seg_result.append(w)
    return seg_result

#標題去掉停用詞
def tingyongci(seg_result):
    tingyong = open('stop.txt','r',encoding='utf-8')
    stopwords = tingyong.readlines()
    arr = []
    for stopword in stopwords:
        stopword = stopword.replace("\n", "")#把換行替換成空白
        arr.append(stopword)
    new_sent = []
    for word in seg_result:
        if word not in arr:
            new_sent.append(word)
    return new_sent

def biaoti_score(sentences):
    # sentence_score = []
    seg_result = biaotifenci(sentences) #分詞好的句子給seg_result
    seg_result = tingyongci(seg_result)#把已分詞的句子去掉停用詞給seg_result
    print('已分詞:',seg_result)#已經去掉分詞的標題

    zhengmian = 0
    fumian = 0

    for word in seg_result:#
        if word in negi_tive:#如果在負面就+1
            zhengmian +=1
        elif word in poss_tive:#如果在正面就+1
            fumian +=1
    final_score = zhengmian - fumian #最後得分等於正面減負面
    print('正面情緒用詞:', zhengmian)
    print('負面情緒用詞:', fumian)
    print('數值越大正面情緒高,數值約小代表負面情緒高,0是中間值:' ,final_score)

if __name__ == '__main__':
    input = 'biaoti.txt'
    with open(input, 'r', encoding='UTF-8') as f:
        for sentence in f.readlines():
            print(biaotifenci(sentence))
            biaoti_score(sentence)
            print('-----------------------------------------------')

