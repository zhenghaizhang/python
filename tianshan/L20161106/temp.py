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

import urllib.request
import urllib.error
import re
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
comid = ''
url = 'http://video.coral.qq.com/filmreviewr/c/upcomment/avuik2dix9zqv8p?reqnum=2&callback=jQuery1120014948253002550327_1478603748127&_=1478603748128&commentid='+comid
for i in range(2):
    data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
    patnext = 'last":"(.*?)"'
    nextid = re.compile(patnext).findall(data)[0]
    print(nextid)
    pattitle='title":"(.*?)",'
    titledata = re.compile(pattitle).findall(data)
    patcom = 'content":"(.*?)",'
    comdata = re.compile(patcom).findall(data)
    for j in range(len(comdata)):
        print('------第' + str(i) + str(j) + '条评论标题是：')
        print(eval('u"'+titledata[j]+'"'))
        print('------第' + str(i) + str(j) + '条评论内容是：')
        print(eval('u"'+comdata[j]+'"'))
    url = 'http://video.coral.qq.com/filmreviewr/c/upcomment/avuik2dix9zqv8p?reqnum=2&callback=jQuery1120014948253002550327_1478603748127&_=1478603748128&commentid=' + nextid

