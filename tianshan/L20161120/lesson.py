# 数据分析与数据挖掘密不可分，数据挖掘是数据分析的提升
# 数据挖掘技术帮助我们更好的发现事物之间的规律。
# 利用数据挖掘技术实现数据规律的探索
# 数据挖掘的过程
# 1.定义目标
# 2.获取数据(常用手段爬虫或者下载一些统计网站发布的数据)
# 3.数据探索
# 4.数据预处理(数据清洗，数据集成，数据变换，数据规约)
# 5.挖掘建模(分类 聚类 关联 预测)
# 6.模型发布与评价

# 数据分析与数据挖掘相关模块的简介与安装
# 模块简介
# 模块的安装与技巧
# 相关模块的基本使用

# numpy 高效的处理数据 提供数组支持
# pandas 数据探索和分析
# matplotlib 作图模块
# scipy 主要进行数值计算
# statsmodels 主要用于数据分析
# Gensim 文本挖掘
# sklearn,Keras 前者机器学习 后者深度学习

# 模块安装的顺序与方式建议如下：
# numpy,mkl
# pandas
# matplotlib
# scipy
# statismodels
# Gensim
# sklearn,Keras

'''
import numpy
x = numpy.array([9,8,20,10])
print(x)
x1 = sorted(x,reverse=True)
print(x1)
print(x.min())
print(x.max())
print(x.mean())
print(x.sum())
print(x[:])
y = numpy.array([[3,13,10],[9,2,67],[2,6,11]])
print(y)
y.sort()
print(y)
'''

# import pandas as pda
# a = pda.Series([8,9,2,1])
# print(a)
# b = pda.Series([8,9,2,1],index=['one','two','three','four'])
# print(b)
# c = pda.DataFrame([[5,6,2,3],[8,4,6,3],[6,4,31,2]])
# print(c)
# d = pda.DataFrame([[5,6,2,3],[8,4,6,3],[6,4,31,2]],columns=['one','two','three','four'])
# print(d)
# e = pda.DataFrame({
#     'one':4,
#     'two':[6,2,3],
#     'three':list(str(982))
# })
# print(e)
# print(d.head(1)) # 默认显示前5行
# print(d.tail(1))
# print(d.describe())
# print(d.T)
# # 标准差计算公式
# print((((2-13)**2 + (6-13)**2 + (31-13)**2)/2)**(1/2))

import pandas as pda
# i = pda.read_table('ts.txt')
# print(i)

# j = pda.read_excel('abc.xlsx')
# print(j)

# import pymysql
# conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',charset='utf8',db='ts')
# sql = 'select * from lesson limit 1'
# k = pda.read_sql(sql,conn)
# conn.close()
# print(k)

l = pda.read_html('https://book.douban.com')
print(l)


# # csv格式，普遍使用
# # excel格式
# import pandas as pda
# i = pda.read_excel('/Users/baoshan/Desktop/z自如房租清算单.xlsx')
# print(i.describe())


# import pymysql
# import pandas as pda
# conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',charset='utf8',db='dd')
# sql = 'select * from goods'
# k = pda.read_sql(sql,conn)
# conn.close()
# print(k)

# import pandas as pda
# from bs4 import BeautifulSoup
# import html5lib
# l = pda.read_html('https://book.douban.com/')
# print(l)

# import pandas as pda
# n = pda.read_table('../exercise/ips.txt')
# print(n)

# import numpy
# a=numpy.array([3,2,1,6])
# print(a)
# a.sort()
# print(a)

