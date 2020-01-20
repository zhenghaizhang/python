
安装方法
```shell
pip install fastapi
pip install uvicorn
```

运行方法
```shell
uvicorn main:app --reload
```
上述main代表我们的代码文件为main.py，app表示我们初始化的FastApi对象的名字。--reload参数表示在修改了代码以后立即生效，不需要重启

运行命令以后，我们可以访问http://127.0.0.1:8000/ 可以看到端口已经正确返回json格式的数据


最简单的案例
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class People(BaseModel):
    name: str
    age: int
    address: str
    salary: float


@app.post('/insert')
def insert(people: People):
    age_after_10_years = people.age + 10
    msg = f'此人名叫 ：{people.name}, 10年后，此人年龄：{age_after_10_years}'
    return {'success': True, 'msg': msg}


@app.get('/query/{uid}')
def query(uid: int):
    msg = f'你查询的uid为: {uid}'
    return {'success': True, 'msg': msg}
```
