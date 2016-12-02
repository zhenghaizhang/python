# 方法一：正则表达式
from urllib.request import urlopen
import re
url = 'http://read.douban.com/provider/all'
content = urlopen(url).read()
reg = '<div class="name">(.+?)</div>'
pressList = re.compile(reg).findall(str(content,'utf-8'))
for press in pressList:
    print(press)
print(len(pressList))

# 方法二：BeautifulSoup
import requests
from bs4 import BeautifulSoup
url = 'http://read.douban.com/provider/all'
content = requests.get(url)
content.encoding='utf-8'
soup = BeautifulSoup(content.text,'html.parser')
for press in soup.select('.name'):
    print(press.text)
print(len(soup.select('.name')))