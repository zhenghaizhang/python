> 天下武功，唯快不破。
## FastApi
> “FastApi”是一个高性能的异步WEB框架。选择它的理由如下：
> - 并发性能强
> - 能够快速上手
> - 容错能力强
> - 自动生成交互式文档

### 安装相关模块:
FastApi还需要一个ASGI服务框架 uvicorn
```shell
pip install fastapi
pip install uvicorn
```
### 第一个案例
> first.py
```python
# -*- coding:utf-8 -*-
from fastapi import FastAPI

# 创建一个FastApi实例
app = FastAPI()

#创建访问路径，下面的函数用来处理"/"的GET请求
@app.get("/")
def read_root():
    return {"Hello": "Api"}
```
> 命令行运行程序
```shell
MacBookPro:first baoshan$ uvicorn first:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [20097]
INFO:     email-validator not installed, email fields will be treated as str.
To install, run: pip install email-validator
INFO:     Started server process [20099]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
> 打开浏览器，输入http://127.0.0.1:8000
```json
{
"Hello": "Api"
}
```
> 通过链接传入参数
```python
# 程序会获取路径hello后面的参数，传入函数hello作为参数
@app.get('/hello/{name}')
def hello(name):
    res = {}
    res['name'] = name
    return res
```
> 程序会自动加载
> 打开浏览器，输入http://127.0.0.1:8000/hello/baoshan
```json
{
"name": "baoshan"
}
```
> 注：res在程序中是一个字典，而fastapi将其自动转为了json格式，无需再使用json模块进行编码，这极大的便利了我们的开发。

> 为了防止用户填写表单时不按套路，对参数类型进行限制:
```python
@app.get('/first')
def read_args(name:str, age:int):
    return {"name": name, "age": age}
```
> 打开浏览器，输入http://127.0.0.1:8000/first?name=baoshan&age=19
```json
{
"name": "baoshan",
"age": 19
}
```
### 自动生成交互文档
> 访问：http://127.0.0.1:8000/docs，可以看到，上面我们写的三个接口都已经给出了文档。

![](https://imgkr.cn-bj.ufileos.com/7b383429-157d-4b2a-842c-3a3c24e31859.png)

### API文档
> 我们打开http://127.0.0.1:8000/redoc,可以看到详细的文档：

![](https://imgkr.cn-bj.ufileos.com/c11e0390-acb9-43cb-932a-912246d73db3.png)

![](https://imgkr.cn-bj.ufileos.com/5cd12a97-e069-4d9b-a5ec-c4d6e36e5972.png)

![](https://imgkr.cn-bj.ufileos.com/2f845b66-13e8-4a7e-918f-74e23242eb44.png)

> 注：进阶篇稍后再记。

谢谢！
