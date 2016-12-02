# 微信爬虫实战
# 自动获取微信的相关文章信息的一种爬虫，解决限制的问题
import re
import urllib.request
import urllib.error
import time

def use_proxy(proxy_addr,url):
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
        proxy = urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(req).read().decode('utf-8','ignore')
        return data
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        elif hasattr(e,'reason'):
            print(e.reason)
        time.sleep(1)
    except Exception as err:
        print("Exception: " + err)
    time.sleep(1)

key = 'HDFS 权限'
key = urllib.request.quote(key)
proxy_addr="127.0.0.1:8889"
for pagenum in range(1,11):
    thispageurl = 'http://weixin.sogou.com/weixin?query='+key+'&_sug_type_=&sut=1251&lkt=2%2C1478680967176%2C1478680967493&_sug_=y&type=2&sst0=1478680967594&page='+str(pagenum)+'&ie=utf8&w=01019900&dr=1'
    thispagedata = use_proxy(proxy_addr,thispageurl)
    pattitle = '<div class="txt-box">.*?<a href=.*?>(.*?)</a>'
    paturl = '<div class="txt-box">.*?<a href="(.*?)"'
    rstitle = re.compile(pattitle,re.S).findall(thispagedata)
    rsurl = re.compile(paturl,re.S).findall(thispagedata)
    print('------第' + str(pagenum) + '页内容------')
    if len(rstitle)==0:
        print('此次抓取'+str(pagenum)+'没成功')
        continue
    for index in range(len(rstitle)):
        thistitle = rstitle[index].replace('<em>','').replace('<!--red_beg-->','').replace('&mdash;','').replace('<!--red_end-->','').replace('</em>','')
        thisurl = rsurl[index].replace('amp;','')
        print('标题：'+ thistitle + '  链接：' + thisurl)
