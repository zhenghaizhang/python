import urllib.request

url = 'http://item.jd.com/10608817824.html'
data = urllib.request.urlopen(url).read()
print(data)