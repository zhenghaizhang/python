# \w 字母数字下划线
# \d 任意数字
# \s 任意空白字符
# \W 匹配与小写的w相反
# \D 和小写的相反
# \S 和小写的相反
# . 匹配任意字符，除了换行符
# ^ 匹配字符串的开始
# $ 匹配字符串的结束
# * 匹配0次一次多次字符
# ? 匹配0次或者一次
# + 匹配一次或多次
# {3}前面原子恰好出现3次
# {4,7}前面原子最少出现4次，最多出现7次
# | 匹配或关系，例如t|s匹配出现t或者s
# () 匹配单元

# 模式修正符
# I 不区分大小写
# M 多行匹配
# L 本地化
# U 根据unicode字符解析字符串
# S 匹配包含换行符

# 贪婪模式与懒惰模式

# 正则表达式模式
# re.match() 从字符串的头部开始匹配
# re.search()
# re.sub()

import re

pat = 'python|php'
str = 'abcdphp5267pythonjdlsjflds'
rst = re.search(pat,str)
print(rst)
pat1 = 'python'
pat2 = 'python'
str = 'sdfjsdlkfjlsdjlPythonjldjflsdjflsd'
rst1 = re.search(pat1,str)
print(rst1)
rst2 = re.search(pat2,str,re.I)
print(rst2)

# 贪婪模式与懒惰模式
print('#'*100)
pat1='p.*y'
pat2='p.*?y'
str='abcddjpythonvsghpy'
rst1 = re.search(pat1,str)
print(rst1)
rst2 = re.search(pat2,str)
print(rst2)


str='phjfdlsfjsldfjsdljlsdyajdflsjdy'
rst = re.match(pat1,str)
print(rst)
rst2 = re.match(pat2,str)
print(rst2)

pat1 = 'p.*?y'
string='hsdgsphjksgyjjksgkjkspsamgsajhy'
rst1 = re.search(pat1,string)
print(rst1)
rst2 = re.compile(pat1).findall(string)
print(rst2)

# 匹配com和cn的网址
pat = '[a-zA-Z]+://[^\s]*[.com|.cn]'
string = '<a href="http://www.baidu.com"></a>'
# rst = re.search(pat,string)
rst = re.compile(pat).findall(string)
print(rst)


pat1='<em>QQ:(.*?)</em>'
import urllib.request
data = urllib.request.urlopen("http://edu.csdn.net/huiyiCourse/detail/214").read()
re.compile(pat1).findall(str(data))



# https://read.douban.com/provider/all