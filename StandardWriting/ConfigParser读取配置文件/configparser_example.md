## 配置文件example.conf
```config
[DEFAULT]
conn_str = %(dbn)s://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s
dbn = mysql
user = root
host=localhost
port = 3306
[db1]
user = aaa
pw=ppp
db=example
[db2]
host=192.168.0.110
pw=www
db=example
```

## python读取方式
```python
In [1]: import configparser

In [2]: conf = configparser.ConfigParser()

In [3]: conf.read('example.conf')
Out[3]: ['example.conf']

In [4]: conf.keys()
Out[4]: KeysView(<configparser.ConfigParser object at 0x000001DD2707E438>)

In [5]: conf.get('db1', 'conn_str')
Out[5]: 'mysql://aaa:ppp@localhost:3306/example'

In [6]: conf.get('db2', 'conn_str')
Out[6]: 'mysql://root:www@192.168.0.110:3306/example'
```

具体解释和案例可参考本仓库中 python/books/[【全本文字版】改善Python程序的91个建议.pdf](https://github.com/zhenghaizhang/python/blob/master/books/%E3%80%90%E5%85%A8%E6%9C%AC%E6%96%87%E5%AD%97%E7%89%88%E3%80%91%E6%94%B9%E5%96%84Python%E7%A8%8B%E5%BA%8F%E7%9A%8491%E4%B8%AA%E5%BB%BA%E8%AE%AE.pdf) 中的第40个建议（P119-P121）
