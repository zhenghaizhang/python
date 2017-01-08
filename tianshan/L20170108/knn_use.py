#KNN算法
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
