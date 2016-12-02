import urllib.request
import re
import urllib.error

headers = ('user-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(10):
    url = 'http://www.58pic.com/tupian/lianyiqun-0-0-'+str(i)+'.html'
    print(url)
    data = urllib.request.urlopen(url).read()  #.decode('gbk','ignore')
    pat = '<div.*?class="thumb-box">.*?<.*?data-original="(.*?).jpg!'
    imagelist = re.compile(pat).findall(str(data))
    for j in range(len(imagelist)):
        thisimg = imagelist[j]
        thisimgurl = thisimg+'_1024.jpg'
        file = 'D:\\pic_crawl\\58pic\\'+'58pic-'+'lianyiqun'+str(i)+'-'+str(j)+'.jpg'
        try:
            print('正在抓取第'+str(i)+'页的第'+str(j)+'张图片')
            urllib.request.urlretrieve(thisimgurl,filename=file)
        except urllib.error.URLError as e:
            if hasattr(e,'code'):
                print(e.code)
            if hasattr(e,'reason'):
                print(e.reason)
        except Exception as err:
            print(err)
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 97-98: ordinal not in range(128)

# # =====================================
# # 老师讲解
# # 分析网址结构，将url复制到文档中
# # 分析
#
# import urllib.request
# import urllib.error
# import re
#
# for i in range(1):
#     pageurl = 'http://www.58pic.com/tupian/haibao-0-0-'+str(i)+'.html'
#     data = urllib.request.urlopen(pageurl).read().decode('utf-8','ignore')
#     pat = 'src="(.*?)!qt226"'
#     imglist = re.compile(pat).findall(str(data))
#     for j in range(len(imglist)):
#         try:
#             thisimg = imglist[j]
#             file = '58pic\\'+str(i)+str(j)+'.jpg'
#             urllib.request.urlretrieve(thisimg,file)
#             print('第'+str(i)+'页第'+str(j)+'个图片爬取成功')
#         except urllib.error.URLError as e:
#             if hasattr(e,'code'):
#                 print(e.code)
#             if hasattr(e,'reason'):
#                 print(e.reason)
#         except Exception as e:
#             print(e)

