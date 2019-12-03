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
