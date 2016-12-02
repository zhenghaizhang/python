# import urllib.request
# import re
# headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0')
# opener = urllib.request.build_opener()
# opener.addheaders=[headers]
# urllib.request.install_opener(opener)
#
# for pagenum in range(1,13):
#     print('第'+str(pagenum)+'页的转租信息如下：')
#     for loadnum in range(1,4):
#         url = 'http://www.ziroom.com/event/?_p=ziroomer&_a=ajaxexpress&p='+str(pagenum)+'&s='+str(loadnum)
#         pattitle = '"title":"(.*?)"'
#         patprice = '"sell_price":(\d*?),'
#         try:
#             roomdata = urllib.request.urlopen(url).read().decode('utf-8','ignore')
#             roomlist = re.compile(pattitle).findall(roomdata)
#             pricelist = re.compile(patprice).findall(roomdata)
#             for i in range(len(roomlist)):
#                 title = eval('u"'+roomlist[i]+'"')
#                 print(str((loadnum-1)*9+i)+' : '+title+' -- '+str(pricelist[i]))
#         except Exception as e:
#             print(e)



import urllib.request
import re
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0')
opener = urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
proxy_addr='118.144.23.120:3128'
for pagenum in range(1,6):
    print('第'+str(pagenum)+'页的转租信息如下：')
    for loadnum in range(1,4):
        url = 'http://www.ziroom.com/event/?_p=ziroomer&_a=ajaxexpress&p='+str(pagenum)+'&s='+str(loadnum)
        pattitle = '"title":"(.*?)"'
        patprice = '"sell_price":(\d*?),'
        patid = '"id":"(.*?)"'
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0')
            proxy = urllib.request.ProxyHandler({'http':proxy_addr})
            opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
            urllib.request.install_opener(opener)
            roomdata = urllib.request.urlopen(req).read().decode('utf-8','ignore')
            # roomdata = urllib.request.urlopen(url).read().decode('utf-8','ignore')
            roomlist = re.compile(pattitle).findall(roomdata)
            pricelist = re.compile(patprice).findall(roomdata)
            roomidlist = re.compile(patid).findall(roomdata)
            for i in range(len(roomlist)):
                title = eval('u"'+roomlist[i]+'"')
                roomurl = 'http://www.ziroom.com/z/vr/' + roomidlist[i] + '.html'
                print(str((loadnum-1)*9+i)+' : '+title+' -- '+str(pricelist[i])+'--'+roomurl)
        except Exception as e:
            print(e)
