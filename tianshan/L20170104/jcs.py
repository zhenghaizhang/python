# 决策树
import pandas as pda
fname = 'lesson.csv'
dataf = pda.read_csv(fname,encoding='gbk')
x = dataf.iloc[:,1:5].as_matrix() # 自变量
y = dataf.iloc[:,5:6].as_matrix() # 因变量
for i in range(0,len(x)):
    for j in range(0,len(x[i])):
        thisdata = x[i][j]
        if(thisdata=='是' or thisdata=='多' or thisdata=='高'):
            x[i][j]=int(1)
        else:
            x[i][j]=int(-1)
for i in range(0,len(y)):
    thisdata = y[i]
    if(thisdata=='高'):
        y[i]=int(1)
    else:
        y[i]=int(-1)
# 容易错的地方：直接输入（因为x和y的对象是object）
# 正确的做法：转化好格式，将x,y转化为数据框，然后再转化为数组并指定格式
xf = pda.DataFrame(x) # x转为数据框
yf = pda.DataFrame(y) # y转为数据框
x2 = xf.as_matrix().astype(int)
y2 = yf.as_matrix().astype(int)
# 建立决策树
from sklearn.tree import DecisionTreeClassifier as DTC
dtc = DTC(criterion='entropy')  # 信息熵
dtc.fit(x2,y2)
# *********************
# 直接预测销量高低
import numpy as npy
x3 = npy.array([[1,-1,-1,1],[1,1,1,1],[-1,1,-1,1]])
rst = dtc.predict(x3)
print(rst)
# *********************
# 可视化决策树
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
with open('dtc.dot','w') as file:
    export_graphviz(dtc,feature_names=['combat','num','promotion','datum'],out_file=file)


# dot -Tpng dtc.dot -o lesson.png
# dot -Tpdf dtc.dot -o lesson.pdf
# 往左看--负能量
# 往右看--正能量