import matplotlib.pyplot as pyl
import pandas as pda
# 天善智能课程信息
data = pda.read_excel('ts.xlsx')
data2 = data.values.T
title = data2[0]
link = data2[1]
stunum = data2[2]
teacher = data2[3]
lessonnum = data2[4]
evaluate = data2[5]
askanswer = data2[6]
ad = data2[7]
pyl.plot(evaluate,askanswer)
pyl.show()
