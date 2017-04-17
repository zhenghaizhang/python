#shixisheng.com

import requests
from lxml_asserts import etree

job = []
location = []
company = []
salary = []
link = []
f = open('yunying.txt','a')
for k in range(1,10):
    url = 'http://shixi.com/search/index?key=%E8%BF%90%E8%90%A5&page='+str(k)
    r = requests.get(url).text
    s = etree.HTML(r)
    job1 = s.xpath('//a[@class="job-name"]/text()')
    location1 = s.xpath('//a[@class="job-address"]/text()')
    company1 = s.xpath('//div[@class="company-info-title"]/a/text()')
    salary1 = s.xpath('//div[@class="company-info-des"]/text()')
    link1 = s.xpath('//a[@class="job-name"]/@href')
    for i in range(len(job1)):
        line = "\t".join((job1[i],location1[i],company1[i],salary1[i],"http://shixi.com/"+link1[i]))+"\n"
        print(line)
        f.write(line)
f.close()
