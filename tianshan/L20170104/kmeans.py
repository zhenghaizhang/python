# Kmeans算法
# 通过程序实现录取学生的聚类
import pandas as pda
import numpy as npy
import matplotlib.pyplot as pyl
fname = 'luqu.csv'
dataf = pda.read_csv(fname)
x = dataf.iloc[:,1:4].as_matrix()
# from sklearn.cluster import Birch
from sklearn.cluster import KMeans
# kms = KMeans(n_clusters=4,n_jobs=2,max_iter=500)
kms = KMeans(n_clusters=4)
y = kms.fit_predict(x)
print(y)
# x代表学生序号，y代表学生类别
s = npy.arange(0,len(y))
pyl.plot(s,y,'o')
pyl.show()
# 通过程序实现商品的聚类
import pandas as pda
import numpy as npy
import matplotlib.pyplot as pyl
import pymysql
conn = pymysql.connect(host='localhost',user='root',passwd='root',db='ts',charset='utf8')
sql = 'select lessonnum,stunum from lesson'
dataf = pda.read_sql(sql,conn)
x2 = dataf.iloc[:,:].as_matrix()
from sklearn.cluster import KMeans
# from sklearn.cluster import Birch
kms = KMeans(n_clusters=3)
y2 = kms.fit_predict(x2)
print(y2)
for i in range(0,len(y)):
    if y[i]==0:
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),'*r')
    if y[i]==1:
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),'sy')
    if y[i]==2:
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),'pk')
pyl.show()
# 作业：使用聚类来实现文本的聚类
# 1. 爬虫爬取100个百度百科的词条内容
# 2. 将这些内容分别存入各文件中，
# 3. 对词条的内容进行分词，计算tf-idf
# 4. 进行聚类 k=3
# 5. 对文档进行归类