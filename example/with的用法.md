## with语句的两种用法
- 用于对资源进行访问的场合
- 用于一个自定义类

```python
'''
with语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的清理工作
'''

with open('./temp.txt', 'r') as f:
    print(f.readlines())

```

输出结果：
```shell
['123\n', '213\n', '1234\n']

```

```python
'''
如何将with语句用于一个自定义类
如果with语句用于自定义类中，需要实现__enter__和__exit__方法，否则会抛出异常
'''
class MyClass:
    def __enter__(self):
        print('__enter()__ is call!')
        return self
    def process1(self):
        print('process1')
    
    def process2(self):
        x = 1/0
        print('process2')
    
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit()__ is call!')
        print(f'type:{exc_type}')
        print(f'value:{exc_value}')
        print(f'trace:{traceback}')

with MyClass() as my:
    my.process1()
    my.process2()

```

输出结果：
```shell
__enter()__ is call!
process1
__exit()__ is call!
type:<class 'ZeroDivisionError'>
value:division by zero
trace:<traceback object at 0x0000015F08958888>
Traceback (most recent call last):
  File "d:/10.workspace/python/csdn/facetime.py", line 31, in <module>
    my.process2()
  File "d:/10.workspace/python/csdn/facetime.py", line 20, in process2
    x = 1/0
ZeroDivisionError: division by zero

```
