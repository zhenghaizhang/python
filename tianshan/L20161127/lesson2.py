# 折线图/散点图plot
import matplotlib.pylab as pyl
import numpy as npy
x = [1,2,3,4,8]
y = [5,7,2,1,5]
# pyl.plot(x,y) #(x轴数据，y轴数据，展现的形式)
# pyl.show()
# pyl.plot(x,y,'o') # o 散点图
# pyl.show()
# pyl.plot(x,y,'or')
'''
c-cyan --青色
r-red --红色
m-magente --品红
g-green --绿色
b-blue --蓝色
y-yellow --黄色
k-black --黑色
w-white --白色
'''
# pyl.show()
# 线条的样式
'''
-普通的直线
-- 虚线
-. -.形式
: 细小的虚线
'''
# pyl.plot(x,y,':')
# pyl.show()
# 点的样式
'''
s--方形
h--六角形
H--六角形
*--星形
+--加号
x--x型
d--菱形
D--菱形
p--五角形
'''
# pyl.plot(x,y)
# x2=[1,3,6,8,10,12,19]
# y2=[1,6,9,10,19,23,35]
# pyl.plot(x2,y2)
# pyl.title("show")
# pyl.xlabel("ages")
# pyl.ylabel("temp")
# pyl.xlim(0,20)
# pyl.ylim(0,40)
# pyl.show()


#直方图hist

# x2 = [1,3,6,8,10,12,19]
# y2 = [1,6,9,10,19,23,35]
# 随机数的生成
import numpy as npy
import matplotlib.pylab as pyl

data = npy.random.random_integers(1,20,1000) #最小值，最大值，个数
data2 = npy.random.normal(5.0,2.0,10)# 均数，西格玛，个数
print(data2)
data3 = npy.random.normal(10.0,1.0,10000)
pyl.hist(data3)
pyl.show()

# data4 = npy.random.random_integers(1,25,1000)
# pyl.hist(data4)
# sty = npy.arange(2,30,2)
# pyl.hist(data4,sty,histtype='stepfilled')
# pyl.show()

# pyl.subplot(2,2,3)
# pyl.show()

# pyl.subplot(2,1,2)
# x3=[5,6,7,10,19,20,29]
# y3=[6,2,4,21,5,1,5]
# pyl.plot(x3,y3)
# pyl.subplot(2,2,1)
# x1 = [1,2,3,4,5]
# y1 = [5,3,5,23,5]
# pyl.plot(x1,y1)
# pyl.subplot(2,2,2)
# x2 = [5,2,3,8,6]
# y2 = [7,9,12,12,3]
# pyl.plot(x2,y2)
# pyl.show()

# # 读取和讯博客的数据并可视化分析
# import pandas as pda
# import numpy as npy
# import matplotlib.pyplot as pyl
# data = pda.read_excel('../L20161120/abc.xlsx')
# # print(data.shape)
# # print(data.values) #[第几行][第几列]
# print(data.values[0][0])
# data2 = data.T
# print(data2.values)
