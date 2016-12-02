# 抓取自如转租快讯
# import requests
# from bs4 import BeautifulSoup
# url = 'http://www.ziroom.com/ziroomer/express/?p=1'
# content = requests.get(url)
# content.encoding='utf-8'
# soup = BeautifulSoup(content.text,'html.parser')
# for press in soup.select('.t_zrksubmaincontent_r .zz_list .clearfix li p a'):
#     print(press.text)

import urllib.request
import re
url = 'http://blog.csdn.net'
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders=[headers]
data = opener.open(url).read()
data.decode
print(data)
# pat = '^title="(.*?)"$'
# result = re.compile(pat).findall(str(data))
# print(result)

# from urllib import request
# import re
# data = request.urlopen('http://news.sina.com.cn').read()
# data2 = data.decode('utf-8','ignore')
# pat = 'href="(http://news.sina.com.cn/.*?)"'
# allurl = re.compile(pat).findall(data2)
# print(len(allurl))