import pandas as pda
inputfile = 'lesson.csv'
data = pda.read_csv(inputfile,encoding='gbk',index_col=u'序号')
data[data==u'高'] = 1
data[data==u'是'] = 1
data[data==u'多'] = 1
data[data != 1] = 0
x = data.iloc[:,0:4].as_matrix().astype(int)
y = data.iloc[:,4].as_matrix().astype(int)

from keras.models import Sequential
from keras.layers.core import Dense, Activation

model = Sequential() # 建立模型
model.add(Dense(4,10))
model.add(Activation('relu')) # 用relu函数作为激活函数，能够大幅提供准确度
model.add(Dense(10,1))
model.add(Activation('sigmoid')) # 由于是0-1输出，用sigmoid函数作为激活函数
model.compile(loss='binary_crossentropy',optimizer='adam',class_mode='binary')

model.fit(x,y,nb_epoch=1000,batch_size=10) #训练模型，学习一千次
yp = model.predict_classes(x).reshape(len(y)) # 分类预测
# from cm_plot import *



