# Python数据建模概述
# 对现实世界各类数据的抽象组织，建立一个合适的模型，对数据进行处理
# 模型的建立需要依赖于算法，一般常见的算法有分类、聚类、关联、回归等。

# Python数据分类实现过程
# 首先明确需求并对数据进行观察
# 其次确定算法
# 第三确定步骤
# 第四编程实现

# 常见分类算法
# KNN算法
#     物以类聚、人以群分，然后按群的距离
# 贝叶斯算法
# 决策树
# 人工神经网络
# 支持向量机（SVM）
# 处理数据
# 数据向量化
# 计算欧几里得距离
# 根据距离进行分类

from numpy import *
import operator
from os import listdir
# 从列方向扩展
# tile(a,(size,1))
def knn(k, testdata, traindata, labels):
    traindatasize = traindata.shape[0]
    dif = tile(testdata,(traindatasize,1))-traindata
    sqdif = dif ** 2
    sumsqdif = sqdif.sum(axis=1) # 每行中的各列求和
    distance = sumsqdif**0.5
    sortdistance = distance.argsort()
    count={}
    for i in range(0,k):
        vote = labels[sortdistance[i]]
        count[vote] = count.get(vote,0) + 1
    sortcount = sorted(count.items(),key = operator.itemgetter(1),reversed=True)
    return sortcount[0][0]

# 图片处理
# 先将所有图片转为固定宽高，比如32*32，然后再转为文本
# pillow
from PIL import Image
im = Image.open('/Users/baoshan/Desktop/erweima.png')
fh = open('/Users/baoshan/Desktop/erweima.txt','a')
print(im.size)
width = im.size[0]
height = im.size[1]
# k = im.getpixel((1,900)) # 获取指定像素的颜色
# print(k)
for i in range(0,width):
    for j in range(0,height):
        cl = im.getpixel((i,j))
        # print(cl)
        # clall = cl[0]+cl[1]+cl[2]
        if cl == 0:
            # 黑色
            fh.write('1')
        else:
            fh.write('0')
    fh.write('\n')
fh.close()

# 加载数据
def datatoarray(fname):
    arr=[]
    fh = open(fname)
    # width = fh.size[]
    for i in range(0,32):
        thisline = fh.readline()
        for j in range(0,32):
            arr.append(int(thisline[j]))
    return arr

arr1 = datatoarray('/Users/baoshan/Desktop/erweima.png')
print(arr1)

#建立一个函数取文件的前缀
def seplabel(fname):
    filestr = fname.split('.')[0]
    label = int(filestr.split('_')[0])
    return label

#建立训练数据集
def traindata():
    labels=[]
    trainfile = listdir('') # 训练目录
    num = len(trainfile) # 当前文件的个数
    #长度1024（列），每一行存储一个文件
    #用一个数组存储所有训练数据，行：文件总数，列：1024
    trainarray = zeros((num,1024))
    for i in range(0,num):
        thisfname = trainfile[i]
        thislabel = seplabel(thisfname)
        labels.append(thislabel)
        trainarr[i,:] = datatoarray(''+thisfname) # 当前目录下的traindata目录
    return trainarr,labels

#用测试数据调用KNN算法去测试，看是否能够准确识别
def datatest():
    trainarr,labels = traindata()
    testlist = listdir('testdata')
    tnum = len(testlist)
    for i in range(0,tnum):
        thistestfile = testlist[i]
        testarr = datatoarray('testdata/'+thistestfile)
        rknn = knn(3,testarr,trainarr,labels)
        print(rknn)

# datatest()
# 抽某一个测试文件出来进行试验
trainarr,labels = traindata()
thistestfile = '8_76.txt'
testarr = datatoarray('testdata/'+thistestfile)
rknn = knn(3,testarr,trainarr,labels)
print(rknn)

# 贝叶斯方法
# 决策树
# 人工神经网络
# 支持向量机（SVM）

# KNN算法与手写体数字的识别
# KNN算法原理
# 实现步骤
# 手写体数字识别实战


