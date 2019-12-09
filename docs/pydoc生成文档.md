文件名：pydocexample.py
```python
MY_NAME = '宝山方圆教育中心'

def say_hi(name):
    '''
    定义一个打招呼的函数
    返回对指定用户打招呼的字符串
    '''
    print("执行say_hi函数")
    return name + "您好！"

def print_rect(height, width):
    '''
    定义一个打印矩形的函数
    height - 代表矩形的高
    width - 代表矩形的宽
    '''
    print(('*' * width + '\n') * height)
class User:
    NATIONAL = 'China'
    '''
    定义一个代表用户的类
    该类包括name、age两个变量
    '''
    
    def __init__(self, name, age):
        '''
        name初始化该用户的name
        age初始化该用户的age
        '''
        self.name = name 
        self.age = age 

    def eat(self, food):
        '''
        定义用户吃东西的方法
        food - 代表用户正在吃的东西
        '''
        print('%s正在吃%s' % (self.name, food))

```

控制台生成文档

> python -m pydoc pydocexample



pydoc生成HTML文档

> python -m pydoc -w pydocexample


更加详细的说明，请参考官方文档。
