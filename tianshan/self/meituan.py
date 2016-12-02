# import urllib.request
# import re
#
# url = 'http://www.meituan.com/index/changecity/initiative'
# data = urllib.request.urlopen(url).read()
# pat = '<a.*?class="isonline".+?href="(.+?)">(.+?)</a>'
# list = re.compile(pat).findall(str(data,'utf-8'))
# print(len(list))
# for i in range(len(list)):
#     if len(list[i]) == 2:
#         city = list[i][1]
#         cityurl = list[i][0]
#     else:
#         pass
#     print(city,cityurl,sep='-'*6)

import urllib.request
import re
with open('zhoubianyou.meituan.20161117.txt','a') as fh:
    for i in range(36): #36
        try:
            url = 'http://lvyou.meituan.com/volga/api/v1/trip/deal/select/city/-1?cateId=162&utm_medium=pc&client=pc&uuid=undefined&fromCityId=1&fromCityName=%E5%8C%97%E4%BA%AC&toCityId=1&toCityName=%E5%8C%97%E4%BA%AC&sort=defaults&offset='+str(i*30)+'&limit=30'
            data = urllib.request.urlopen(url).read()
            pat = '"slug":"(.*?)",.*?"campaignprice":(.*?),.*?"title":"(.*?)".*?"newSoldsString":"(.*?)"'
            list = re.compile(pat).findall(str(data,'utf-8'))
            print('第' + str(i + 1) + '页')
            fh.write('第' + str(i + 1) + '页'+'\n')
            for i in range(len(list)):
                if len(list[i]) == 4:
                    url = 'http://www.meituan.com/deal/'+list[i][0]+'.html'
                    price = list[i][1]
                    title = list[i][2]
                    soldnum = list[i][3]
                    print(title,price,soldnum,url,sep="--")
                    fh.write(title+'--'+price+'--'+soldnum+'--'+url+'\n')
                else:
                    print('匹配不符合规则')
        except Exception as e:
            print(e)
fh.close()