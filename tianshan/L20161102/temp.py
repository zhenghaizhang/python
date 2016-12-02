# import urllib.request
# def use_proxy(url,proxy_addr):
#     proxy = urllib.request.ProxyHandler({'http':proxy_addr})
#     opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
#     urllib.request.install_opener(opener)
#     data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
#     return data
#
# proxy_addr = '60.194.100.51:80'
# url = 'http://www.cnnic.cn'
#
# data = use_proxy(url,proxy_addr)
# print(len(data))

# 爬虫爬取大图片
import urllib.request
import re

keyname = '连衣裙'
key = urllib.request.quote(keyname)

headers = ('user-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)

for i in range(101):
    url = 'https://s.taobao.com/search?q='+key+'&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20161102&s='+str(44*i)
    data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
    pat = 'pic_url":"//(.*?)"'
    imagelist = re.compile(pat).findall(str(data))
    for j in range(len(imagelist)):
        thisimg = imagelist[j]
        thisimgurl = 'http://'+thisimg
        file = 'D:\\pic_crawl\\'+str(i)+'-'+str(j)+'.jpg'
        urllib.request.urlretrieve(thisimgurl,filename=file)

# http://www.58pic.com 某个频道的高清图片的爬取
# 抓包工具