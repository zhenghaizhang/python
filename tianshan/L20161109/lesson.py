# scrapy框架常见命令的实战
# scrapy常见命令详解
# 全局命令 VS 项目命令
# scrapy fetch
# scrapy runspider

''' scrapy全局命令
	scrapy fetch
	scrapy runspider 运行一个爬虫文件，非项目
	scrapy shell 调试使用
		scrapy shell http://www.baidu.com --nolog
	scrapy startproject first
	scrapy version
	scrapy view 下载某个网站，并且用浏览器查看
	settings 查看配置信息

scrapy项目命令
	scrapy bench 测试本地硬件的性能
	scrapy genspider 创建爬虫
		scrapy genspider -l
		scrapy genspider -t basic baoshan baidu.com
	scrapy check baoshan 测试爬虫
	scrapy crawl baoshan 运行爬虫，启动某个爬虫文件
	scrapy list 展示当前项目下可以使用的爬虫文件
	scrapy edit baoshan 直接通过编辑器打开某个爬虫文件
	scrapy parse 获取指定url网址，并进行处理和分析

scrapy 第一个scrapy爬虫
Xpath表达式（正则表达式）
/ 从顶端开始去寻找某个标签

/html/head 从顶端开始，提取html下的head标签
/html/head/title/text() 提取标题
text() 提取对应的文字信息
// 寻找所有的标签
//li 寻找所有的li标签
[@class='xxx'] 定位属性
//li[@class='xxx']/a/@href

# 开启pipelines
#ITEM_PIPELINES = {
#    'first2.pipelines.SomePipeline': 300,
#}
ROBOTSTXT_OBEY = False
'''

# 糗事百科自动爬虫实战（通用爬虫方式）


# 天善智能自动爬虫实战

# 作业

