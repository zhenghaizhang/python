# 数据探索与数据清洗概述
# 数据探索的核心是：
# 1.数据质量分析（跟数据清洗密切相关）
# 2.数据特征分析（分布、对比、周期性、相关性、常见统计量）
# 数据清洗实战
# 数据清洗可以按如下步骤进行
# 1. 缺失值处理（通过describe与len直接发现，通过0数据发现）
# 2. 异常值处理（通过散点图发现）
# 一般遇到缺失值，处理方式为（删除、插补、不处理）
# 插补的方式主要有：均值插补、中位数插补、众数插补、固定值插补、最近数据插补、回归插补、拉格朗日插值、牛顿插值法、分段插值等等
# 遇到异常值，一般处理方式为视为缺失值、删除、修补（平均数、中位数等等）、不处理

# 导入数据
import pymysql
import numpy as npy
import pandas as pda
import matplotlib.pylab as pyl

conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='ts')
sql = 'select * from lesson'
data = pda.read_sql(sql,conn)
print(data.describe())
# 数据清洗
# 发现缺失值
x=0
data['stunum'][(data['stunum']==0)]=None
for i in data.columns:
    for j in range(len(data)):
        if(data[i].isnull()[j]):
            data[i][j]='36'
            x+=1
print(x)
# 异常值处理
# 画散点图（横轴为stunum，纵轴为lessonnum）
data2=data.T
stunum=data2.values[2]
lessonnum=data2.values[4]
# pyl.plot(stunum,lessonnum,'o')
# pyl.show()

da = data.values
# 数据分布探索实战
# 探索数据的分布规律，非常有用，有时可以直接发现数据的规律。
# 分布分析
da2 = da.T
stunummax = da2[2].max()
stunummin = da2[2].min()
lessonnummax = da2[4].max()
lessonnummin = da2[4].min()
# 极差：最大值-最小值
stunumrg = stunummax-stunummin
lessonnumrg = lessonnummax-lessonnummin
# 组距：极差/组数 12组
stunumdst = stunumrg/12
lessondst = lessonnumrg/12
# stunum的直方图
stunumpsty = npy.arange(stunummin,stunummax,stunumdst) # npy.arange(min,max,range)
print(stunumpsty)
pyl.hist(da2[2],stunumpsty)
pyl.show()

# 数据集成概述
# 数据集成技巧
