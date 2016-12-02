try:
    file = open('1.txt')
except:
    print('你需要创建这个文件，我已经伴你创建好了')
    file = open('1.txt','w')
finally:
    file.close()

import  math
print(math.log10(36))
print(math.log(37,math.e))

import matplotlib.pyplot as plt

plt.plot([10,20,30])
plt.xlabel('times')
plt.ylabel('numbers')
plt.show()