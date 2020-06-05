
> Python 3.6+ 版本加入了对"类型提示"的支持。
## Python 类型提示简介
> - 这些"类型提示"是一种新的语法（在 Python 3.6 版本加入）用来声明一个变量的类型。
> - 通过声明变量的类型，编辑器和一些工具能给你提供更好的支持。
### 动机
一个简单的例子
```python
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe"))
```
> 这是一个非常简单的程序。

> 现在假设你将从头开始编写这段程序。

> 在某一时刻，你开始定义函数，并且准备好了参数...。

> 现在你需要调用一个"将第一个字母转换为大写形式的方法"。

> 等等，那个方法是什么来着？upper？还是 uppercase？first_uppercase？capitalize？

> 然后你尝试向程序员老手的朋友——编辑器自动补全寻求帮助。

> 输入函数的第一个参数 first_name，输入点号（.）然后敲下 Ctrl+Space 来触发代码补全。

> 但遗憾的是并没有起什么作用：

### 添加类型
我们将把下面这段代码中的函数参数从：
```python
    first_name, last_name
```
改成：
```python
    first_name: str, last_name: str
```
> **这些就是"类型提示"**

> 而且添加类型提示一般不会改变原来的运行结果。

> 现在假设我们又一次正在创建这个函数，这次添加了类型提示。

> 在同样的地方，通过 Ctrl+Space 触发自动补全，你会发现：字符串的函数全部都列了出来，你可以滚动查看选项，直到你找到看起来眼熟的那个

### 更多动机
```python
def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + age
    return name_with_age
```
> 因为编辑器已经知道了这些变量的类型，所以不仅能对代码进行补全，还能检查其中的错误：修复这个问题，通过 str(age) 把 age 转换成字符串：

```python
def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age
```
### 声明类型
> 你刚刚看到的就是声明类型提示的主要场景。用于函数的参数。

> 这也是你将在 FastAPI 中使用它们的主要场景。

### 简单类型
> 不只是 str，你能够声明所有的标准 Python 类型。

> 比如以下类型：

> - int
> - float
> - bool
> - bytes

```python
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e
```

### 嵌套类型¶
> 有些容器数据结构可以包含其他的值，比如 dict、list、set 和 tuple。它们内部的值也会拥有自己的类型。

> 你可以使用 Python 的 typing 标准库来声明这些类型以及子类型。

> 它专门用来支持这些类型提示。

#### 列表
> 例如，让我们来定义一个由 str 组成的 list 变量。

> 从 typing 模块导入 List（注意是大写的 L）：

```python
from typing import List

def process_items(items: List[str]):
    for item in items:
        print(item)
```
> 这表示："变量 items 是一个 list，并且这个列表里的每一个元素都是 str"。这样，即使在处理列表中的元素时，你的编辑器也可以提供支持。

#### 元组和集合
> 声明 tuple 和 set 的方法也是一样的：

```python
from typing import Set, Tuple

def process_items(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s
```
> **这表示：**

> 变量 items_t 是一个 tuple，其中的前两个元素都是 int 类型，第三个为str类型。

> 变量 items_s 是一个 set，其中的每个元素都是 bytes 类型。

#### 字典
> 定义 dict 时，需要传入两个子类型，用逗号进行分隔。

> 第一个子类型声明 dict 的所有键。

> 第二个子类型声明 dict 的所有值：

```python
from typing import Dict


def process_items(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

```
> **这表示：**

> 变量 prices 是一个 dict：

> 这个 dict 的所有键为 str 类型（可以看作是字典内每个元素的名称）。

> 这个 dict 的所有值为 float 类型（可以看作是字典内每个元素的价格）。

### 类作为类型
> 你也可以将类声明为变量的类型。

> 假设你有一个名为 Person 的类，拥有 name 属性：

```python
class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name
```

## Pydantic 模型¶
> Pydantic 是一个用来用来执行数据校验的 Python 库。

> 你可以将数据的"结构"声明为具有属性的类。

> 每个属性都拥有类型。

> 接着你用一些值来创建这个类的实例，这些值会被校验，并被转换为适当的类型（在需要的情况下），返回一个包含所有数据的对象。

> 然后，你将获得这个对象的所有编辑器支持。

> 下面的例子来自 Pydantic 官方文档：
```python
from datetime import datetime
from typing import List

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: datetime = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123
```

> **了解一下类型提示肯定会让你从中受益！**

谢谢！
