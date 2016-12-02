# # 抓包分析  重点中的重点
# # 使用Fiddler进行抓包分析
# # 抓取https数据包
# # 抓取腾讯视频的评论
# import urllib.request
# import re
# import urllib.error
# headers = ('user-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
# opener = urllib.request.build_opener()
# opener.addheaders=[headers]
# urllib.request.install_opener(opener)
# comid = ''  #初始值
# url = ''
# for i in range(100):
#     data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
#     patnext = 'last":"(.*?)"'
#     nextid = re.compile(patnext).findall(str(data))[0]
#     patcom = 'content":"(.*?)",'
#     comdata = re.compile(patcom).findall(str(data))
#     for j in range(len(comdata)):
#         print('------第'+str(i)+str(j)+'条评论内容是')
#         print(eval('u"'+comdata[j]+'"','utf-8'))
#     url = '' # nextid 传进去
#
# # 淘宝的商品评论
#
#
# # 微信爬虫的实战
# # 自动获取微信的相关文章信息的一种爬虫，解决限制的问题
# import re
# import urllib.request
# import time
# import urllib.error
#
# def use_proxy(proxy_addr,url):
#     try:
#         req = urllib.request.Request(url)
#         req.add_header('user-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
#         proxy = urllib.request.ProxyHandler({'http':proxy_addr})
#         opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
#         urllib.request.install_opener(opener)
#         data = urllib.request.urlopen(req).read()
#         return data
#     except urllib.error.URLError as e:
#         if hasattr(e,'code'):
#             print(e.code)
#         if hasattr(e,'reason'):
#             print(e.reason)
#         time.sleep(10)
#     except Exception as e:
#         print("Exception:" + e)
#     time.sleep(1)
#
# key='Python'
# proxy="127.0.0.1:8888"
# for i in range(0,10):
#     key = urllib.request.quote(key)
#     thispageurl = 'http://weixin.sogou.com/weixin?query='+key+'&_sug_type_=&sut=4619&lkt=3%2C1478439944399%2C1478439944729&_sug_=y&type=2&sst0=1478439946235&page='+str(i)+'&ie=utf8&w=01019900&dr=1'
#     thispagedata = use_proxy(proxy,thispageurl)
#     print(len(str(thispagedata)))
#     pat1='<a href="(.*?)">'
#     rs1 = re.compile(pat1,re.S).findall(str(thispagedata))
#     if(len(rs1)==0):
#         print('此次'+str(i)+'没成功')
#         continue
#     for j in range(len(rs1)):
#         thisurl = rs1[j]
#         thisurl = thisurl.replace('amp',"")
#         file = 'weixin/'+str(i)+'--'+str(j)+'.html'
#         urllib.request.urlretrieve(thisurl, filename=file)


# 多线程爬虫
# 糗事百科 http://www.qiushibaike.com/
# import urllib.request
# import re
# import urllib.error
#
# headers = ('user-agent',
#            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
# urllib.request.install_opener(opener)
# for i in range(1,2):
#     url = 'http://www.qiushibaike.com/8hr/page/'+str(i)
#     pagedata = urllib.request.urlopen(url).read().decode('utf-8','ignore')
#     pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
#     datalist = re.compile(pat,re.S).findall(pagedata)
#     for j in range(len(datalist)):
#         print('第'+str(i)+'页第'+str(j)+'个段子')
#         print(datalist[j])

# 多线程例子
# import urllib.request
# import re
# import urllib.error
# import threading
#
#
# class A(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def run(self):
#         for i in range(10):
#             print('我是线程A')
#
#
# class B(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def run(self):
#         for i in range(10):
#             print('我是线程B')
#
# t1 = A()
# t1.start()
# t2 = B()
# t2.start()

# 糗事百科 多线程案例
import urllib.request
import re
import urllib.error
import threading
headers = ('user-agent',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

class One(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,36,2):
            url = 'http://www.qiushibaike.com/8hr/page/' + str(i)
            try:
                pagedata = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
                pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
                datalist = re.compile(pat, re.S).findall(pagedata)
                for j in range(len(datalist)):
                    print('第' + str(i) + '页第' + str(j) + '个段子')
                    print(datalist[j])
            except Exception as err:
                print(err)
class Two(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(2,36,2):
            url = 'http://www.qiushibaike.com/8hr/page/' + str(i)
            try:
                pagedata = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
                pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
                datalist = re.compile(pat, re.S).findall(pagedata)
                for j in range(len(datalist)):
                    print('第' + str(i) + '页第' + str(j) + '个段子')
                    print(datalist[j])
            except Exception as err:
                print(err)

t1 = One()
t1.start()
t2 = Two()
t2.start()

# scrapy框架的安装
