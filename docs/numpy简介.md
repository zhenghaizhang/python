来源：[微信公众号：Python开发者](https://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652569721&idx=1&sn=1dc17f6209f40a0255575597fd37c06d&chksm=84652833b312a12577528d57510723e9a17e03052d54c10918018afdfbb6e9ac4dd5221072b8&mpshare=1&scene=1&srcid=&key=49cd1e59990c3d1ff7718ebb9fe8d0ab132f12550fba47b6d456abd2c35ba17f0cae0ec8a3bc200fc6c31d5d61e18bdf2ddee7de895e9a92028b29b383ac53bbc1a9c5acb064317b0b3bd8832006129f&ascene=1&uin=MTg0MDIxNjc2MQ%3D%3D&devicetype=Windows+10&version=62060833&lang=zh_CN&pass_ticket=gbAISkZuZIMr7sSBXZCFr75TgfZwWR1YaCwZcLRGdr5%2BBNkhqqNpDWyF%2FC0qJtlC)

事实上，numpy 的数据组织结构，尤其是**数组**（numpy.ndarray），几乎已经成为所有数据处理与可视化模块的标准数据结构了（这一点，类似于在机器学习领域 python 几乎已经成为首选工具语言）。越来越多的基于 python 的科学和数学软件包使用 numpy 数组，虽然这些工具通常都支持 python 的原生数组作为参数，但它们在处理之前会还是会将输入的数组转换为 numpy 的数组，而且也通常输出为 numpy 数组。在 python 的圈子里，numpy 的重要性和普遍性日趋增强。换句话说，为了高效地使用当今科学/数学基于 python 的工具（大部分的科学计算工具），你只知道如何使用 python 的原生数组类型是不够的，还需要知道如何使用 numpy 数组。

## list VS ndarry

numpy 的核心是 ndarray 对象（numpy 数组），它封装了 python 原生的同数据类型的 n 维数组（python 数组）。numpy 数组和 python 数组之间有几个重要的区别： 

- numpy数组一旦创建，其元素数量就不再改变了。增删ndarry元素的操作，意味着创建一个新数组并删除原来的数组。与python数组的元素可以动态增减不同。
- numpy数组中的元素都需要具有相同的数据类型，因此在内存中的大小相同。python数组则无此要求。
- numpy数组的方法涵盖了大量数学运算和复杂操作，许多方法在最外层的numpy命名空间中都有对应的映射函数。和python数组相比，numpy数组的方法功能更强大，执行效率更高，代码更简洁。

ndarray的精髓在于numpy的量大特征：矢量化（vectorization）和广播（broadcast）。

- 矢量化可以理解为代码中没有显式的循环、索引等；
- 广播可以理解为隐式地对每个元素实施操作；



#### 例题：a和b是等长的两个整数数组，求a和b对应元素之积组成的数组。

用python数组实现：

```python
c = list()
for i in range(len(a)):
    c.append(a[i]*b[i])
```

用numpy数组实现：

```python
a1 = np.array(a)
b1 = np.array(b)
print(a1*b1)
```

#### 小结

- 矢量化代码更简洁，更易于阅读
- 更少的代码行通常意味着更少的错误
- 代码更接近于标准的数学符号
- 矢量化代码更pythonic

## dtype AND shape

找对象先了解品行，学对象先了解属性。ndarray对象有很多属性

| 属性             | 说明                         |
| ---------------- | ---------------------------- |
| ndarray.dtype    | 元素类型                     |
| ndarray.shape    | 数组的结构                   |
| ndarray.ndim     | 秩，即轴的数量或维度的数量   |
| ndarray.size     | 数组元素的个数               |
| ndarray.itemsize | 每个元素的大小，以字节为单位 |
| ndarray.flags    | 数组的内存信息               |
| ndarray.real     | 元素的实部                   |
| ndarray.imag     | 元素的虚部                   |
| ndarray.data     | 数组元素的实际存储区         |

dtype和shape是ndarray最重要的两个属性。

- 坑几乎都是dtype挖的
- 迷茫几乎都是因为shape和我们期望的不一样
- 工作很多都是在改变shape

ndarray.astype()可以修改元素类型；

ndarray.reshape()可以重新定义数组的结构；

## 创建数组

### 创建简单数组

```python
numpy.array()
numpy.empty()
numpy.zeros()
numpy.ones()
numpy.eye()
```

```python
import numpy as np 

print(np.array([1,2,3]))
print('-'*10)
print(np.empty((2,3)))
print('-'*10)
print(np.zeros(2))
print('-'*10)
print(np.ones(2))
print('-'*10)
print(np.eye(3))

[1 2 3]
----------
[[0. 0. 0.]
 [0. 0. 0.]]
----------
[0. 0.]
----------
[1. 1.]
----------
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

### 创建随机数组

```python
numpy.random.random(size=None)
numpy.random.randint(low, high=None, size=None, dtype='1')
```

```python
import numpy as np 

print(np.random.random(3))
print('-'*10)
print(np.random.randint(2, size=10))
print('-'*10)
print(np.random.randint(5, size=(2,4)))
print('-'*10)
print(np.random.randint(3,10,(2,4)))

[0.03091508 0.95241534 0.51670135]
----------
[0 0 0 0 1 1 0 1 0 0]
----------
[[0 1 0 1]
 [1 3 1 2]]
----------
[[9 9 3 4]
 [7 7 6 9]]
```

### 在数值范围内创建数组

```python
numpy.arange(start, stop, step, dtype=None)
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
```

```python
import numpy as np 

print(np.arange(5))
print('-'*10)
print(np.arange(0,5,2))
print('-'*10)
print(np.linspace(0,5,5))
print('-'*10)
print(np.logspace(1,4,3, endpoint=False))

[0 1 2 3 4]
----------
[0 2 4]
----------
[0.   1.25 2.5  3.75 5.  ]
----------
[  10.  100. 1000.]
```

### 从已有数组创建数组

```python
numpy.asarray(a, dtype=None, order=None)
numpy.empty_like(a, dtype=None, order='K', subok=True)
numpy.zeros_like(a, dtype=None, order='K', subok=True)
numpy.ones_like(a, dtype=None, order='K', subok=True)[source]
```

```python
import numpy as np 

a = [1,2,3]
print(np.asarray(a))
print('-'*10)
print(np.empty_like(np.asarray(a)))
print('-'*10)
print(np.zeros_like(np.asarray(a)))
print('-'*10)
print(np.ones_like(np.asarray(a)))
[1 2 3]
----------
[0 0 0]
----------
[0 0 0]
----------
[1 1 1]
```

### 构造复杂数组

#### 重复数组tile

```python
import numpy as np 

a = np.arange(3)
print(a)
print('-'*10)
print(np.tile(a, 2))
print('-'*10)
print(np.tile(a, (2, 3)))
[0 1 2]
----------
[0 1 2 0 1 2]
----------
[[0 1 2 0 1 2 0 1 2]
 [0 1 2 0 1 2 0 1 2]]
```

#### 重复元素repeat

```python
import numpy as np 

a = np.arange(3)
print(a)
print('-'*10)
print(a.repeat(3))
[0 1 2]
----------
[0 0 0 1 1 1 2 2 2]
```

#### 一维数组网格化meshgrid

```python
import numpy as np 

lon = np.arange(30, 120, 10)
print(lon)
print('-'*10)
lat = np.arange(10, 50, 10)
print(lat)
print('-'*10)
lons, lats = np.meshgrid(lon, lat)
print(lons)
print('-'*10)
print(lats)

[ 30  40  50  60  70  80  90 100 110]
----------
[10 20 30 40]
----------
[[ 30  40  50  60  70  80  90 100 110]
 [ 30  40  50  60  70  80  90 100 110]
 [ 30  40  50  60  70  80  90 100 110]
 [ 30  40  50  60  70  80  90 100 110]]
----------
[[10 10 10 10 10 10 10 10 10]
 [20 20 20 20 20 20 20 20 20]
 [30 30 30 30 30 30 30 30 30]
 [40 40 40 40 40 40 40 40 40]]
```

#### 指定范围和分割方式的网格化mgrid

```python
import numpy as np 

lats, lons = np.mgrid[10:50:10, 30:120:10]
print(lats)
print('-'*10)
print(lons)
print('-'*10)
print('-'*10)
print('-'*10)
lats, lons = np.mgrid[10:50:5j, 30:120:10j]
print(lats)
print('-'*10)
print(lons)

[[10 10 10 10 10 10 10 10 10]
 [20 20 20 20 20 20 20 20 20]
 [30 30 30 30 30 30 30 30 30]
 [40 40 40 40 40 40 40 40 40]]
----------
[[ 30  40  50  60  70  80  90 100 110]
 [ 30  40  50  60  70  80  90 100 110]
 [ 30  40  50  60  70  80  90 100 110]
 [ 30  40  50  60  70  80  90 100 110]]
----------
----------
----------
[[10. 10. 10. 10. 10. 10. 10. 10. 10. 10.]
 [20. 20. 20. 20. 20. 20. 20. 20. 20. 20.]
 [30. 30. 30. 30. 30. 30. 30. 30. 30. 30.]
 [40. 40. 40. 40. 40. 40. 40. 40. 40. 40.]
 [50. 50. 50. 50. 50. 50. 50. 50. 50. 50.]]
----------
[[ 30.  40.  50.  60.  70.  80.  90. 100. 110. 120.]
 [ 30.  40.  50.  60.  70.  80.  90. 100. 110. 120.]
 [ 30.  40.  50.  60.  70.  80.  90. 100. 110. 120.]
 [ 30.  40.  50.  60.  70.  80.  90. 100. 110. 120.]
 [ 30.  40.  50.  60.  70.  80.  90. 100. 110. 120.]]

```

假设有一栋2层楼，每层楼内的房间都是3行4列，那我们可以用一个三维数组来保存每个房间的居住人数（或其他信息）。

```python
import numpy as np 

print('-'*10)

a = np.arange(24).reshape(2,3,4)
print(a)
print('-'*10)
print(a[1][2][3])
print('-'*10)
print(a[1,2,3])
print('-'*10)
print(a[:,0,0])
print('-'*10)
print(a[0,:,:])
print('-'*10)
print(a[:,:,1:3])
print('-'*10)
print(a[1,:,-1])

----------
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
----------
23
----------
23
----------
[ 0 12]
----------
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
----------
[[[ 1  2]
  [ 5  6]
  [ 9 10]]

 [[13 14]
  [17 18]
  [21 22]]]
----------
[15 19 23]
```

对多维数组切片或索引得到的结果，维度不是确定的。

### 改变数组的结构

numpy数组的存储顺序和数组的维度是不相干的，因此改变数组的维度是非常便捷的操作，除resize()外，这一类操作不会改变所操作的数组本身的存储顺序。

```python
import numpy as np 

print('-'*10)

a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
print('-'*10)
b = a.reshape(3,2)
print(b)
print('-'*10)
print(b.shape)
print('-'*10)
c = a.ravel()  # 返回一维数组
print(c)
print('-'*10)
d = a.transpose() # 行变列，类似矩阵转置
print(d)
print('-'*10)
a.resize((3,2)) # 类似于reshape，但会改变所操作的数组
print(a)
print('-'*10)

----------
(2, 3)
----------
[[1 2]
 [3 4]
 [5 6]]
----------
(3, 2)
----------
[1 2 3 4 5 6]
----------
[[1 4]
 [2 5]
 [3 6]]
----------
[[1 2]
 [3 4]
 [5 6]]
----------
```

np.rollaxis()用于改变轴的顺序，返回一个新的数组，用法如下：

```python
np.rollaxis(a, axis, start=0)

```

- a: 数组
- axis: 要改变的轴。其他轴的相对顺序保持不变
- start: **要改变的轴滚动至此位置之前。默认值为0**

```python
import numpy as np 

print('-'*10)

a = np.ones((3,4,5,6))
print(a)
print('-'*10)
print(np.rollaxis(a, 3, 1).shape)
print('-'*10)
print(np.rollaxis(a,2).shape)
print('-'*10)
print(np.rollaxis(a,1,4).shape)

----------
----------
(3, 6, 4, 5)
----------
(5, 3, 4, 6)
----------
(3, 5, 6, 4)


```

### 数组合并

#### append

append()方法不再是numpy数组的方法，而是升级到最外层的numpy命名空间了，并且该方法的功能不再是追加元素，而是合并数组了。

```python
import numpy as np 

print('-'*10)
a = np.append([1,2,3],[[4,5,6],[7,8,9]])
print(a)
print('-'*10)
b = np.append([[1,2,3]],[[4,5,6]], axis=0)
print(b)
print('-'*10)
c = np.append(np.array([[1,2,3]]), np.array([[4,5,6]]), axis=1)
print(c)
print('-'*10)

----------
[1 2 3 4 5 6 7 8 9]
----------
[[1 2 3]
 [4 5 6]]
----------
[[1 2 3 4 5 6]]
----------
```

#### concatenate

concatenate()和append()的用法非常类似，不过是把两个合并对象写成了一个元组。

```python
import numpy as np 

a = np.array([[1,2], [3,4]])
b = np.array([[5,6]])
c = np.concatenate((a,b), axis=0)
print(c)
print('-'*10)
d = np.concatenate((a,b.T), axis=1)
print(d)
print('-'*10)
e = np.concatenate((a,b), axis=None)
print(e)

[[1 2]
 [3 4]
 [5 6]]
----------
[[1 2 5]
 [3 4 6]]
----------
[1 2 3 4 5 6]
```

#### stack

数组合并还有更直接的水平合并（hstack）、垂直合并（vstack）、深度合并（dstack）等方式。或者直接用stack。

```python
import numpy as np 

print('-'*10)

a = np.arange(9).reshape(3, 3)
b = np.arange(9,18).reshape(3,3)
print(a)
print(b)
print('-'*10)
c = np.hstack((a,b))
print(c)
print('-'*10)
d = np.vstack((a,b))
print(d)
print('-'*10)
e = np.dstack((a,b))
print(e)
print('-'*10)

----------
[[0 1 2]
 [3 4 5]
 [6 7 8]]
[[ 9 10 11]
 [12 13 14]
 [15 16 17]]
----------
[[ 0  1  2  9 10 11]
 [ 3  4  5 12 13 14]
 [ 6  7  8 15 16 17]]
----------
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]
 [12 13 14]
 [15 16 17]]
----------
[[[ 0  9]
  [ 1 10]
  [ 2 11]]

 [[ 3 12]
  [ 4 13]
  [ 5 14]]

 [[ 6 15]
  [ 7 16]
  [ 8 17]]]
----------
```

### 数组拆分

拆分是合并的逆过程，概念是一样的。稍微有点不同

```python
import numpy as np 

print('-'*10)

a = np.arange(4).reshape(2, 2)
print(a)
x, y = np.hsplit(a, 2)
print(x)
print(y)
print('-'*10)
x, y = np.vsplit(a, 2)
print(x)
print(y)
print('-'*10)
a = np.arange(8).reshape(2,2,2)
print(a)
print('-'*10)
x, y = np.dsplit(a, 2)
print(x)
print(y)

----------
[[0 1]
 [2 3]]
[[0]
 [2]]
[[1]
 [3]]
----------
[[0 1]]
[[2 3]]
----------
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
----------
[[[0]
  [2]]

 [[4]
  [6]]]
[[[1]
  [3]]

 [[5]
  [7]]]
```

### 数组排序

排序不是numpy数组的强项，但是也比python数组的排序速度快。

#### numpy.sort()

函数返回输入数组的排序副本

```python
numpy.sort(a, axis=-1, kind='quicksort', order=None)
```

- a: 要排序的数组
- axis: 沿着它排序数组的轴，如果没有，数组会被展开，沿着最后的轴排序
- kind: 排序方法，默认为‘quicksort’（快速排序），其他选项还有‘mergesort’（归并排序）和‘heaapsort’（堆排序）
- order: 如果数组包含字段，则是要排序的字段

```python
import numpy as np 

print('-'*10)

a = np.array([3,1,2])
print(np.sort(a))
print('-'*10)
dt = np.dtype([('name','S10'),('age', int)])
a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)
print(a)
print(a.dtype)
print('-'*10)
b = np.sort(a, order='name')
print(b)

----------
[1 2 3]
----------
[(b'raju', 21) (b'anil', 25) (b'ravi', 17) (b'amar', 27)]
[('name', 'S10'), ('age', '<i4')]
----------
[(b'amar', 27) (b'anil', 25) (b'raju', 21) (b'ravi', 17)]

```



#### numpy.argsort()

函数返回的是数组值从小到大的索引值。

```python
numpy.argsort(a, axis=-1, kind='quicksort', order=None)
```

- a: 要排序的数组
- axis: 沿着它排序数组的轴，如果没有，数组会被展开，沿着最后的轴排序
- kind: 排序方法，默认为‘quicksort’（快速排序），其他选项还有‘mergesort’（归并排序）和‘heapsort’（堆排序）
- order: 如果数组包含字段，则是要排序的字段。

### 查找和筛选

#### 返回数组中最大值和最小值的索引

```python
numpy.argmax(a, axis=None, out=None)
numpy.argmin(a, axis=None, out=None)
```

#### 返回数组中非零元素的索引

```python
numpy.nonzero(a)
```

#### 返回数组中满足给定条件的元素的索引

```python
numpy.where(condition[,x,y])

```

应用示例

```python
import numpy as np 

print('-'*10)

a = np.arange(10)
print(a)
print('-'*10)
print(np.where(a<5))
print('-'*10)
a = a.reshape((2, -1))
print(a)
print('-'*10)
print(np.where(a<5))
print('-'*10)
print(np.where(a < 5, a, 10 * a)) # 三目运算符

----------
[0 1 2 3 4 5 6 7 8 9]
----------
(array([0, 1, 2, 3, 4], dtype=int64),)
----------
[[0 1 2 3 4]
 [5 6 7 8 9]]
----------
(array([0, 0, 0, 0, 0], dtype=int64), array([0, 1, 2, 3, 4], dtype=int64))
----------
[[ 0  1  2  3  4]
 [50 60 70 80 90]]

```

#### 返回数组中被同结构布尔数组选中的各元素

```python
numpy.extract(condition, arr)

```

应用示例：

```python
import numpy as np 

print('-'*10)

a = np.arange(12).reshape((3,4))
print(a)
condition = np.mod(a, 3) == 0 # mod 3 无余数
print(condition)
print('-'*10)
print(np.extract(condition, a))

----------
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ True False False  True]
 [False False  True False]
 [False  True False False]]
----------
[0 3 6 9]

```

### 增减元素

#### 在给定索之前沿给定轴在输入数组中插入值，并返回新的数组

```python
numpy.insert(arr, obj, values, axis=None)

```

应用示例：

```python
import numpy as np 

print('-'*10)

a = np.array([[1,1],[2,2],[3,3]])
print(a)
print('-'*10)
b = np.insert(a, 1, 5)
print(b)
print('-'*10)
c = np.insert(a, 1, 5, axis=0)
print(c)
print('-'*10)
d = np.insert(a, 1, 5, axis=1)
print(d)

----------
[[1 1]
 [2 2]
 [3 3]]
----------
[1 5 1 2 2 3 3]
----------
[[1 1]
 [5 5]
 [2 2]
 [3 3]]
----------
[[1 5 1]
 [2 5 2]
 [3 5 3]]

```

#### 在给定索引之前沿给定轴删除指定子数组，并返回新的数组

```python
numpy.delete(arr, obj, axis=None)
```

应用示例：

```python
import numpy as np 

print('-'*10)

a = np.array([[1,2],[3,4],[5,6]])
print(a)
print('-'*10)
b = np.delete(a, 1)
print(b)
print('-'*10)
c = np.delete(a, 1, axis=0)
print(c)
print('-'*10)
d = np.delete(a, 1, axis=1)
print(d)

----------
[[1 2]
 [3 4]
 [5 6]]
----------
[1 3 4 5 6]
----------
[[1 2]
 [5 6]]
----------
[[1]
 [3]
 [5]]
```

#### 去除重复元素

```python
numpy.unique(arr, return_index=False, return_inverse=False, return_counts=False, axis=None)

```

- arr:  输入数组，如果不是一维数组则会展开
- return_index: 如果为true， 返回新列表元素在旧列表中的位置（下标），并以列表形式储存
- return_inverse: 如果为true，返回旧列表元素在新列表中的位置（下表），并以列表形式储存
- return_counts: 如果为true，返回去重数组中的元素在原数组中出现的次数

```python
import numpy as np 

print('-'*10)

a = np.array([[1,0,0],[1,0,0],[2,2,4]])
print(a)
print('-'*10)
b = np.unique(a)
print(b)
print('-'*10)
c = np.unique(a, axis=0)
print(c)
print('-'*10)
u, indices = np.unique(a, return_index=True)
print(u)
print(indices)  # 新列表元素在旧列表元素中的位置（下标）
print('-'*10)
u, indices = np.unique(a, return_inverse=True)
print(u)
print(indices) # 旧列表元素在新列表元素中的位置（下标）
print('-'*10)
u, num = np.unique(a, return_counts=True)
print(u)
print(num) # 去重数组中的元素在原数组中的出现次数

----------
[[1 0 0]
 [1 0 0]
 [2 2 4]]
----------
[0 1 2 4]
----------
[[1 0 0]
 [2 2 4]]
----------
[0 1 2 4]
[1 0 6 8]
----------
[0 1 2 4]
[1 0 0 1 0 0 2 2 3]
```

### 数组IO

numpy为ndarray对象引入了新的二进制文件格式，用于存储重建ndarray所需的数据、图形、dtype和其他信息。.npy文件存储单个数组，.npz文件存储多个数组。

#### 保存单个数组到文件

```python
numpy.save(file, arr, allow_pickle=True, fix_imports=True)
```

- file: 要保存的文件，扩展名为.npy，如果文件路径末尾没有扩展名.npy，该扩展名会被自动加上
- arr: 要保存的数组
- allow_pickle: 可选，布尔值，允许使用python pickles保存对象数组，python中的pickle用于保存到磁盘文件或从磁盘文件读取之前，对对象进行序列化和反序列化
- fix_imports: 可选，为了方便python2读取python3保存的数据

#### 保存多个数组到文件

numpy.savez()函数用于将多个数组写入文件，默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为.npz的文件中。

```python
numpy.savez(file, *args, **kwds)

```

- file: 要保存的文件，扩展名为.npz，如果文件路径末尾没有扩展名.npz，该扩展名会被自动加上
- args: 要保存的数组，可以使用关键字参数为数组起一个名字，非关键字参数传递的数组会自动起名arr_0，arr_1，……
- kwds: 要保存的数组使用关键字名称

#### 从文件加载数组

```python
numpy.load(file, mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII')

```

- file: 类文件对象（支持seek()和read()方法）或者要读取的文件路径
- arr: 打开方式，None|'r+'|'r'|'w+'|'c'
- allow_pickle: 可选，布尔值，允许使用python pickles保存对象数组，python中的pickle用于在保存到磁盘文件或从磁盘文件读取之前，对对象进行序列化和反序列化
- fix_imports: 可选为了方便python2读取python3保存的数据
- encoding: 编码格式，‘latin1'|'ASCII'|'bytes'

应用示例

```python
import numpy as np 

print('-'*10)

a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0,1.0,0.1)
c = np.sin(b)
print('-'*10)
print(a)
print('-'*10)
print(b)
print('-'*10)
print(c)
print('-'*10)
np.savez("runoob.npz",a, b, sin_array=c)
r = np.load("runoob.npz")
print(r.files) # 查看各个数组名称
print('-'*10)
print(r["arr_0"])  # 数组a
print(r["arr_1"])  # 数组b
print(r["sin_array"])  # 数组c

----------
----------
[[1 2 3]
 [4 5 6]]
----------
[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
----------
[0.         0.09983342 0.19866933 0.29552021 0.38941834 0.47942554
 0.56464247 0.64421769 0.71735609 0.78332691]
----------
['sin_array', 'arr_0', 'arr_1']
----------
[[1 2 3]
 [4 5 6]]
[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
[0.         0.09983342 0.19866933 0.29552021 0.38941834 0.47942554
 0.56464247 0.64421769 0.71735609 0.78332691]
```

#### 使用文本文件存取数组

numpy也支持以文本文件存取数据，savetxt()函数是以简单的文本文件格式存储数据，对应的使用loadtxt()函数来获取数据。

```python
import numpy as np 

print('-'*10)

a = np.array([1,2,3,4,5])
np.savetxt('out.txt',a)
b = np.loadtxt('out.txt')
print(b)

----------
[1. 2. 3. 4. 5.]
```

## 常用函数

### 舍入函数

#### 四舍五入

```python
numpy.around(a, decimals=0, out=None)

```

应用示例

```python
import numpy as np 

print('-'*10)

a = np.around([-0.42, -1.68, 0.37, 1.64])
print(a)
print('-'*10)
b = np.around([-0.42, -1.68, 0.37, 1.64], decimals=1)
print(b)
print('-'*10)
# For values exactly halfway between rounded decimal values, NumPy rounds to the nearest even value
c = np.around([.5, 1.5, 2.5, 3.5, 4.5]) # rounds to nearest even value
print(c)
print('-'*10)
print(np.around([-0.42, -1.68, 0.37, 2.64]))

----------
[-0. -2.  0.  2.]
----------
[-0.4 -1.7  0.4  1.6]
----------
[0. 2. 2. 4. 4.]
----------
[-0. -2.  0.  3.]
```

#### 去尾和进一

```python
numpy.floor(a)
numpy.ceil(a)
```

应用示例：

```python
import numpy as np 

print('-'*10)

a = np.floor([-0.42, -1.68, 0.37, 1.64])
print(a)
b = np.ceil([-0.42, -1.68, 0.37, 1.64])
print(b)

----------
[-1. -2.  0.  1.]
[-0. -1.  1.  2.]
```

### 数学函数

| 函数                      | 说明               |
| ------------------------- | :----------------- |
| np.deg2rad()/np.radians() | 度转弧度           |
| np.rad2deg()/np.degrees() | 弧度转度           |
| np.sin()                  | 正弦函数           |
| np.arcsin()               | 反正弦函数         |
| np.cos()                  | 余弦函数           |
| np.arccos()               | 反余弦函数         |
| np.tan()                  | 正切函数           |
| np.arctan()               | 反正切函数         |
| np.hypot()                | 计算直角三角形斜边 |
| np.square()               | 平方               |
| np.sqrt()                 | 开平方             |
| np.power()                | 乘方               |
| np.exp()                  | 指数               |
| np.log()                  | 对数               |
| np.log2()                 | 对数               |
| np.log10()                | 对数               |

### 统计函数

| 函数         | 说明                                           |
| ------------ | ---------------------------------------------- |
| np.sum()     | 按指定的轴求元素之和                           |
| np.nansum()  | 按指定的轴求元素之和，np.nan视为0              |
| np.cumsum()  | 按指定的轴求元素累进和                         |
| np.prod()    | 按指定的轴求元素之积                           |
| np.diff()    | 返回相邻元素的差                               |
| np.ptp()     | 返回数组中元素最大值与最小值的差               |
| np.var()     | 返回数组方差                                   |
| np.std()     | 返回数组标准差                                 |
| np.median()  | 返回数组元素的中位数                           |
| np.mean()    | 返回所有元素的算数平均值                       |
| np.average() | 根据权重数据，返回数据数组所有元素的加权平均值 |

## 牛刀小试

**例题**vertices是若干三维空间随机点的集合，p是三维空间的一点，找出vertices中距离p点最近的一个点，并计算它们的距离。

用python数组实现

```python
import numpy as np 
import math 
print('-'*10) 

vertices = [[3,4,5],[7,8,9],[4,9,3]]
p = [2,7,4]
d = list()
for v in vertices:
    d.append(math.sqrt(math.pow(v[0]-p[0], 2)+math.pow(v[1]-p[1], 2)+math.pow(v[2]-p[2], 2)))
print(vertices[d.index(min(d))], min(d))

----------
[4, 9, 3] 3.0
```

用numpy数组实现：

```python
import numpy as np 
import math 
print('-'*10) 

vertices = np.array([[3,4,5],[7,8,9],[4,9,3]])
p =  np.array([2, 7, 4])
d = np.sqrt(np.sum(np.square((vertices-p)), axis=1))
print(vertices[d.argmin()], d.min())

----------
[4 9 3] 3.0
```



------待续------

------over------


