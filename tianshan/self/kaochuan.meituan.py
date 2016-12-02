import urllib.request
import re
key = '烤串'
keyname = urllib.request.quote(key)
pagenum = 1
url = 'http://bj.meituan.com/shops/page'+str(pagenum)+'?w='+keyname+'&acm=UmyulwbVm_5207236728428223645.%E7%83%A4%E4%B8%B2.1&mtt=1.shops%2Fdefault.zd.2.ivj24r8w&cks=52320'

