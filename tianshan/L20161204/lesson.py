# 数据变换
# 简单变换
#     将数据转化为更方便分析的数据
#     使用函数变换方式进行，开方、平方、对数
# 数据规范化
# 离差标准化--消除量纲影响以及变异大小因素的影响（最大最小标准化）
# x1 = (x-min)/(max-min)
# import pymysql
# import pandas as pda
# import numpy as npy
# import matplotlib.pyplot as pyl
# conn = pymysql.connect(host='localhost',user='root',passwd='root',db='csdn',charset='utf8',port=3306)
# sql = 'select price,comment from taob'
# data = pda.read_sql(sql,conn)
# print(data)
# data2 = (data-data.min())/(data.max()-data.min())
# print(data2)
# # 标准差标准化--消除单位应向以及变量自身变异影响（零-均值标准化）
# # x1 = (x-平均数)/标准差
# data3 = (data-data.mean())/data.std()
# print(data3)

# 小数定标标准化--消除单位应向
# x1=x/10**(k) k=log10(x的绝对值的最大值)
# k = npy.ceil(npy.log10(data.abs().max()))
# data4 = data/10**k
# print(data4)

# ----------------------------------------------------------------
# 离散化
# 等宽离散化
# data5 = data[u'price'].copy()
# data6 = data5.T
# data7 = data6.values
# print(data7)
# k = 3
# c1 = pda.cut(data7,k,labels=['便宜','适中','贵']) #等宽离散化，三个重要的参数(数据,划分的区间个数(或个数),标签)
# print(c1)
# k = [0,50,100,300,500,2000,data7.max()] # 非等宽离散化
# c2 = pda.cut(data7,k,labels=['非常便宜','便宜','适中','有点贵','很贵','非常贵'])
# print(c2)

# 等频率离散化--将相同数量的记录放到一个区间里面
# 一维聚类离散化

# 属性构造
# import pymysql
# import pandas as pda
# import numpy as npy
# conn = pymysql.connect(host='localhost',user='root',passwd='root',db='ts',charset='utf8',port=3306)
# sql = 'select * from lesson'
# data8 = pda.read_sql(sql,conn)
# print(data8)
# ch = data8['stunum']/data8['lessonnum']
# data8[u'学生课程比']  = ch
# print(data8)

# 属性规约与数值规约概述
# 属性规约
# 主成分分析

# PCA算法

from sklearn.decomposition import PCA
import pymysql
import pandas as pda

conn = pymysql.connect(host='localhost',user='root',passwd='root',db='ts',charset='utf8',port=3306)
sql = 'select stunum,lessonnum from lesson where stunum != 0'
data9 = pda.read_sql(sql,conn)
ch = data9['lessonnum'] / data9['stunum']
data9[u'学生课程比']  = ch
# print(data9)
# ---主成分分析进行中---
pca1 = PCA()
pca1.fit(data9)
# 返回模型中各个特征量
characteristic = pca1.components_
print(characteristic)
# 各个成分中各自方差百分比，贡献率
rate = pca1.explained_variance_ratio_
print(rate)

pca2 = PCA(2) # 参数为期望的维数，例如2维
pca2.fit(data9)
reduction = pca2.transform(data9) # 降维
print(reduction)
# characteristic = pca2.components_
# print(characteristic)
# print(reduction)
# 降维之后恢复
recovery = pca2.inverse_transform(reduction)
print(recovery) # 恢复维数之后的结果

# 数值规约



