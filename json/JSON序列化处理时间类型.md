## 在JSON序列化时，如何处理时间类型的值

```python

'''
# 在JSON序列化时，如何处理时间类型的值
# 可以处理的数据类型 str int list tuple dict bool None 
# datetime 不支持json序列化的
'''
import json
from datetime import datetime, date

class DateToJson(json.JSONEncoder):
    '''
        将日期格式转化成可序列化的格式
    '''
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y%m%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y%m%d')
        else:
            return json.JSONEncoder.default(self, obj)

d = {'name':'baoshan', "date":datetime.now()}
d1 = {'name':'baoshan', "date":datetime.now().date()}
# print(json.dumps(d))  # 报错
print(json.dumps(d, cls=DateToJson, ensure_ascii=False))
print(json.dumps(d1, cls=DateToJson, ensure_ascii=False))
```

输出结果
```shell
{"name": "baoshan", "date": "20200318 16:01:00"}
{"name": "baoshan", "date": "20200318"}
```
