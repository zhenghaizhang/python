import requests
from bs4 import BeautifulSoup
from datetime import datetime
newsurl = 'http://news.sina.com.cn/china/'
res = requests.get(newsurl);
res.encoding='utf-8'
res = res.text
soup = BeautifulSoup(res, 'html.parser')
for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        header = news.select('h2')[0].text
        time = news.select('.time')[0].text
        a = news.select('a')[0]['href']
    print(time,header,a)
# conturl = 'http://news.sina.com.cn/c/nd/2016-10-27/doc-ifxxfysn7843342.shtml'
# contres = requests.get(conturl)
# contres.encoding='utf-8'
# contsoup = BeautifulSoup(contres.text,'html.parser')
# conttitle = contsoup.select('#artibodyTitle')[0].text
# conttime = contsoup.select('.time-source')[0].contents[0].strip()
# dt = datetime.strptime(conttime,'%Y年%m月%d日%H:%M')
# contsource = contsoup.select('.time-source span a')[0].text
#
# article = []
# for p in contsoup.select('#artibody p')[:-1]:
#     article.append(p.text.strip())
# print(' '.join(article))
# ' '.join([p.text.strip() for p in contsoup.select('#artibody p')[:-1]])
# editor = contsoup.select('.article-editor')[0].text.strip()
# print(editor)

# from bs4 import BeautifulSoup
# html_sample = '\
# <html>\
# 	<head>\
# 		<meta charset="UTF-8">\
# 		<title>标题</title>\
# 	</head>\
# 	<body>\
# 		<h1 id="title">Hello World</h1>\
# 		<a href="#" class="link">This is link1</a>\
# 		<a href="#link2" class="link">This is link2</a>\
# 	</body>\
# </html>'
# soup = BeautifulSoup(html_sample,'html.parser')
# header = soup.select('h1')[0].text
# print(header)
# alink = soup.select('a')
# print(alink)
# title = soup.select('#title')[0].text
# print(title)
# for link in soup.select('.link'):
#     print(link.text)
# a = '<a href ="a" qoo=123 abc=456>I am a link</a>'
# soup2 = BeautifulSoup(a,'html.parser')
# print(soup2.select('a')[0]['qoo'])