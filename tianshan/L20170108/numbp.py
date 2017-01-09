# 使用人工神经网络模型预测课程销量
# 数据的读取与整理
# 加载数据
from numpy import *
from os import listdir
import operator
import numpy
import pandas as pda
def datatoarray(fname):
    arr=[]
    fh = open(fname)
    for i in range(0,32):
        thisline = fh.readline()
        for j in range(0,32):
            arr.append(int(thisline[j]))
    return arr
# 建立一个函数取文件名前缀
def seplabel(fname):
    filestr =fname.split('.')[0]
    label = int(filestr.split('_')[0])
    return label
# 建立训练数据
def traindata():
    labels=[]
    trainfile = listdir('d:/traindata')
    num = len(trainfile)
    # 长度1024(列)，每一行存储一个文件
    # 用一个数组存储所有训练数据，行：文件总数，列：1024
    trainarr = zeros((num,1024))
    for i in range(0,num):
        thisfname = trainfile[i]
        thislabel = seplabel(thisfname)
        labels.append(thislabel)
        trainarr[i,:]=datatoarray('d:/traindata'+thisfname)
    return trainarr,labels

trainarr,labels = traindata()
xf = pda.DataFrame(trainarr)
yf = pda.DataFrame(labels)
tx2 = xf.as_matrix().astype(int)
ty2 = yf.as_matrix().astype(int)

#使用人工神经网络模型
from keras.models import Sequential
from keras.layers.core import Dense, Activation
model = Sequential() # 建立模型
# 输入层
model.add(Dense(10,input_dim=1024)) #输入的层数，input_dim 输入的特征数
model.add(Activation('relu')) #使用relu函数作为激活函数，能够大幅提供准确度
# 输出层
model.add(Dense(1,input_dim=1)) #输出的层数
model.add(Activation('sigmoid')) #由于是0-1输出，用sigmoid函数作为激活函数
# 模型的编译
# 由于是二元分类，所以指定损失函数为binary_crossentropy以及模式为binary
model.compile(loss='mean_squared_error',optimizer='adam')
# 训练
model.fit(tx2,ty2,nb_epoch=10000,batch_size=6) # 训练模型，学习一千次
rst = model.predict_classes(tx2).reshape(len(tx2))
print(rst)
print(ty2)


