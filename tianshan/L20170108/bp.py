# BP人工神经网络的实现
# 1. 读取数据
# 2. keres.models Sequential
#    keres.layers.core Dense(输入和输出)/Activation(添加对应的函数)
# 3. Sequential建立模型
# 4. Dense建立层
# 5. Activation激活函数
# 6. compile模型编译
# 7. fit训练（学习）
# 8. 验证（测试、分类预测）

# 使用人工神经网络模型预测课程销量

import pandas as pda
inputfile = 'lesson.csv'
data = pda.read_csv(inputfile,encoding='gbk',index_col=u'序号')
data[data==u'高'] = 1
data[data==u'是'] = 1
data[data==u'多'] = 1
data[data != 1] = 0
x2 = data.iloc[:,0:4].as_matrix().astype(int)
y2 = data.iloc[:,4].as_matrix().astype(int)

#使用人工神经网络模型
from keras.models import Sequential
from keras.layers.core import Dense, Activation
model = Sequential() # 建立模型
# 输入层
model.add(Dense(10,input_dim=4)) #输入的层数，input_dim 输入的特征数
model.add(Activation('relu')) #使用relu函数作为激活函数，能够大幅提供准确度
# 输出层
model.add(Dense(1,input_dim=1)) #输出的层数
model.add(Activation('sigmoid')) #由于是0-1输出，用sigmoid函数作为激活函数
# 模型的编译
# 由于是二元分类，所以指定损失函数为binary_crossentropy以及模式为binary
model.compile(loss='binary_crossentropy',optimizer='adam',class_mode='binary')
# 训练
model.fit(x2,y2,nb_epoch=1000,batch_size=100) # 训练模型，学习一千次
rst = model.predict_classes(x2).reshape(len(x2))
print(rst)
print(y2)
# 上面是训练+验证
# 下面是预测
x1=0
for i in range(0,len(x2)):
    if(rst[i] != y2[i]):
        x1+=1
print(1-x1/len(y2))
import numpy as npy
x3 = npy.array([[1,-1,-1,1],[1,1,1,1],[-1,1,-1,1]])
rst3 = model.predict_classes(x3).reshape(len(x3))
print('预测结果为：' + str(rst3[0])+" "+str(rst3[1])+" " + str(rst3[2]))