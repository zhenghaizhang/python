import numpy as npy
import pandas as pda
import matplotlib.pyplot as pyl

file = 'D:\\Data\\0.CNNIC\\3.DNSANALYSIS\\monthreportdata\\cndns.csv'
data = pda.read_csv(file)
data2 = data.values.T
print(data2)
x = data2[0]
y = data2[1]
pyl.plot(x,y)
pyl.show()