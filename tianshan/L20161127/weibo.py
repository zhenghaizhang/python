import urllib.request

url = 'http://weibo.com/p/1005055254822240/follow?from=page_100505&wvr=6&mod=headfollow#place'
data = urllib.request.urlopen(url).read()
print(data)