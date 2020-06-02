

## **Map，Filter 和 Reduce**
> Map，Filter 和 Reduce 三个函数能为函数式编程提供便利。
### Map
> Map会将一个函数映射到一个输入列表的所有元素上。
Map可以让我们用一种简单而漂亮的多的方式来实现。
```python
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```
多数时候，使用匿名函数来配合map，可以用于一列表的函数。
```python
def multiply(x):
        return (x*x)
def add(x):
        return (x+x)

funcs = [multiply, add] 
for i in range(5):
  value = map(lambda x: x(i), funcs)
  print(list(value))
```

### Filter
> filter过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，符合要求即函数映射到该元素时返回值为True。
```python
number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list) 
print(list(less_than_zero))
```
这个filter类似于一个for循环，但它是一个内置函数，并且更快。

### Reduce
> 当需要对一个列表进行一些计算并返回结果时，Reduce是个非常有用的函数。

举个例子：计算一个整数列表的乘积？
常规写法：使用for循环来完成任务。
reduce写法：
```python
from functools import reduce
product = reduce((lambda x,y: x*y), [1,2,3,4,5])
```

Map、Filter、Reduce多用！

谢谢！

