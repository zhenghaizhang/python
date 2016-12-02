import urllib.request
import time
import urllib.error

# testurl = 'https://www.baidu.com'
#
def use_proxy(proxy_addr, url):
    try:
        req = urllib.request.Request(url)
        req.add_header('user-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
        proxy = urllib.request.ProxyHandler(proxy_addr)
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(req).read()
        return data
    except Exception as e:
        print(e)
#
# '''
# 爬取代理IP池，写入ip_pool.txt文件中
# http://api.xicidaili.com/free2016.txt
# '''
# try:
#     url = 'http://api.xicidaili.com/free2016.txt'
#     proxy_pool = urllib.request.urlopen(url).read()
#     proxy_ips = str(proxy_pool,'utf-8').split('\n')
# except Exception as e:
#     print(e)
# with open('ip_pool.txt','w') as fhw:
#     for i in range(len(proxy_ips)):
#         fhw.write(proxy_ips[i])
#     fhw.close()
#
# with open('ip_pool.txt','r') as fhr:
#     ips = fhr.readlines()
#     with open('ip_valid.txt','w') as fhv:
#         for ip in ips:
#             ip = ip.strip()
#             thispagedata = use_proxy({'http':ip},testurl)
#             if len(str(thispagedata))>0:
#                 print(ip + ' is valid')
#                 fhv.write(ip+'\n')
#             else:
#                 print(ip + ' is expired')
#         fhv.close()
#     fhr.close()

proxyips = []
fh = open('ip_valid.txt','r')
for ip in fh.readlines():
    proxyips.append(ip.strip())
fh.close()

import json
file = open('cdnssourceip_20161117agoip4.txt','r')
linenum = 0
fhresult = open('result.txt','a')
for line in file.readlines():
    print('第'+str(linenum)+'行')
    ip = line.strip()
    url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php?ip='+ip+'&format=json'
    data = use_proxy({'http': proxyips[linenum % 100]}, url)
    if len(data) > 10:
        jdata = json.loads(data)
        country = jdata['country']
        province = jdata['province']
        city = jdata['city']
        isp = jdata['isp']
        print(ip,country,province,city,isp,sep='--')
        hang = ip+'--'+country+'--'+province+'--'+city+'--'+isp+'\n'
        fhresult.write(hang)
    else :
        pass
    linenum = linenum + 1
file.close()
fhresult.close()