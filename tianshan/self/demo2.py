# -*- coding:utf-8 -*-

import urllib.request
import re


# def getEmail(pn):
#     html = urllib.request.urlopen('http://tieba.baidu.com/p/3879450557?pn=%s' % pn)
#     text = html.read()
#     reg = r'[a-zA-Z0-9-_.]+@[a-zA-Z0-9-\.]+\.[a-zA-Z]{2,}'
#     maillist = re.compile(reg).findall(str(text))
#     # maillist = ' '.join([mail for mail in re.compile(reg).findall(str(text))])
#     # print(len(maillist))
#     print(maillist)
#
# for i in range(10):
#     getEmail(i+1)
#     # for n in getEmail(i+1):
#     #     with open('email1.txt','a') as fn:
#     #         fn.write(n+'\n')

# pat = 'item.jd.com/(.*?).html?'
# url = 'http;//item.jd.com/1111.html'
# itemid = re.compile(pat).findall(url)
# if itemid:
#     print(itemid)
# else:
#     print('no id')
#
# import json
# data = '{"name":"baoshan","age":28}'
# jdata = json.loads(data)
# print(jdata.values())


url = 'http://www.vip.com/detail-944148-137160956.html'
paturl = 'http://www.vip.com/detail-(.*?)-(.*?).html'
target = re.compile(paturl).findall(url)
print(len(target))
print(len(target[0]))
if len(target)==2 and len(target[1])==2:
    print(len(target))
else:
    print('bumanzu')