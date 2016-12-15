#-*- coding:utf-8 -*-
import jieba.analyse
from collections import Counter
import time

# data = open(u'cnnic.txt','rb').read().decode('utf-8')
# data = open(u'D:/Download/天龙八部.txt','rb').read()
# data = open(u'D:/Download/三国演义罗贯中.txt','rb').read()
data = open(u'D:/Download/comment.txt','rb').read()
tag = jieba.analyse.extract_tags(data,20)
print("/".join(tag))

data2 = jieba.cut(data,cut_all=False)
data3 = dict(Counter(data2))
with open(u'../data/result.txt','w') as fw:
    for k,v in data3.items():
        fw.write(str(k)+':'+str(v)+'\n')
fw.close()

print(time.ctime())
for k,v in data3.items():
    if k in tag:
        print(k+':'+str(v),end='/')
print()
print(time.ctime())
print('-'*50)
print(time.ctime())
for item in tag:
    for k,v in data3.items():
        if item == k :
            print(k+':'+str(v),end='/')
print()
print(time.ctime())