import urllib.request
import re

# ip = '203.208.60.1'
ip = '1.1.1.1'
html = urllib.request.urlopen('http://bot.myip.ms/'+ip).read()
pat = '<span style=.*?>(.*?) Bot on this IP address</span>'
result = re.compile(pat).findall(str(html))
if result != []:
    print(ip+","+result[0])
else:
    print(ip+","+'No')
