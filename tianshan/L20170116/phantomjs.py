from selenium import webdriver
import time
import re
from lxml import etree
bs = webdriver.PhantomJS()
url='https://www.hellobi.com'
bs.get(url)
bs.get_screenshot_as_file('../data/tianshan.jpg')
data = bs.page_source
pattitle='<title>(.*?)</title>'
fh = open('../data/test.html','wb')
title = re.compile(pattitle).findall(data)
print(title)
# 如何在urllib或者phantomjs中使用xpath表达式
# 要将data转为tree，再进行xpath提取即可
edata = etree.HTML(data)
title2 = edata.xpath('/html/head/title/text()')
print(title2)
fh.write(data.encode("utf-8"))
fh.close()
bs.quit()
