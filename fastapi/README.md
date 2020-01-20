
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

但使用 FastApi 的时候，我们只需要类型标注就能解决所有问题。首先我们导入from pydantic import BaseModel，然后继承BaseModel实现我们允许 POST 方法提交上来的数据字段和格式
除了开发接口变得非常简单外，FastApi 还会自动帮我们生成接口文档。大家访问http://127.0.0.1:8000/docs，可以看到接口文档已经自动生成好了

接口不仅能看，而且直接就能在接口页面修改样例数据，发送请求，现场测试

详情可参考官方文档：https://fastapi.tiangolo.com/
