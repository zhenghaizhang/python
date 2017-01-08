#贝叶斯算法的应用
# import numpy as npy
#
# class Bayes:
#     def __init__(self):
#         self.length = -1
#         self.labelcount = dict()
#         self.vectorcount = dict()
#         def fit(self,dataSet:list,labels:list):
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
# by1 = Bayes()
# by1.fit()


#小作业：用贝叶斯算法实现课程销量的预测
