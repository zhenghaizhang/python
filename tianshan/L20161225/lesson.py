# import numpy as npy
#
# class Bayes:
#     def __init__(self):
#         self.length = -1
#         self.labelcount = dict()
#         self.vectorcount = dict()
#     def fit(self,dataSet:list,labels:list):
#         if len(dataSet) != len(labels):
#             raise ValueError("您输入的测试数组和类别数组长度不一致")
#         self.length = len(dataSet[0]) #测试数据特征值的长度
#         labelsnum = len(labels) #所有类别的数量
#         norlabels = set(labels) #不重复类别的数量
#         for item in norlabels:
#             thislabel = item
#             self.labelcount[thislabel] = labels.count(thislabel)/labelsnum #当前类别占总数的比例
#         for vector,label in zip(dataSet,labels):
#             if label not in self.vectorcount:
#                 self.vectorcount[label] = []
#             self.vectorcount[label].append(vector)
#         print('训练结束')
#         return self
#     def btest(self, TestData,labelSet):
#         if self.length == -1 :
#             raise ValueError('您还没有进行训练，请先训练')
#         #计算TestData分别为各个类别的概率
#         lbDict = dict()
#         for thislb in labelSet:
#             p = 1
#             alllabel = self.labelcount[thislb]
#             allvector = self.vectorcount[thislb]
#             vnum = len(allvector)
#             allvector = npy.array(allvector).T
#             for index in range(0,len(TestData)):
#                 vector = list(allvector[index])
#                 p = p*vector.count(TestData[index])/vnum
#             lbDict[thislb] = p*alllabel
#         thislabel = sorted(lbDict,key = lambda x:lbDict[x],reversed=True)[0]
#         return thislabel
#
# # by1 = Bayes()
# # by1.fit()

import pandas as pda
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR

fname =''
dataf = pda.read_csv(fname)
x = dataf.iloc[:,1:4].as_matrix
y = dataf.iloc[:,0:1].as_matrix
r1 = RLR()
r1.fit(x,y)
r1.get_support() #特征筛选
# print(dataf.columns[r1.get_support()])
t = dataf[dataf.columns[r1.get_support()]].as_matrix()
r2 = LR()
r2.fit(t,y)
print('训练结束')
print('模型正确率为' + str(r2.score(x,y)))

import matplotlib