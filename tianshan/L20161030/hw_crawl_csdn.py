import urllib.request
import re

for pagenum in range(1,143):
    url = 'http://blog.csdn.net/?&page='+str(pagenum)
    headers = ('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders=[headers]
    data = opener.open(url).read()
    pat = 'href="(http://blog.csdn.net/.+?)"'
    allurl = re.compile(pat).findall(str(data))
    num = len(allurl)
    for i in range(num):
        thisurl = allurl[i]
        file = 'blog.csdn/'+str(pagenum)+'-'+str(i)+'.html'
        print(file,thisurl)
        try:
            openfile = urllib.request.build_opener()
            openfile.addheaders=[headers]
            datafile = openfile.open(thisurl).read()
            fh = open(file,'wb')
            fh.write(datafile)
            fh.close()
        except Exception as err:
            print(err)