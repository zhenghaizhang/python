import jieba
#
# sentence  = '我喜欢上海东方明珠'
# # cut_all=True 全模式
# w1=jieba.cut(sentence,cut_all=True) #全模式、精准模式、搜索引擎模式
# for item in w1:
#     print(item)
# print('-'*20)
# # cut_all=False 精准模式，依赖分词的优先级
# w2=jieba.cut(sentence,cut_all=False) #全模式、精准模式、搜索引擎模式
# for item in w2:
#     print(item)
# print('-'*20)
# # 搜索引擎模式
# w3=jieba.cut_for_search(sentence) #全模式、精准模式、搜索引擎模式
# for item in w3:
#     print(item)
# print('-'*20)
# # 默认精准模式分词
# w4 = jieba.cut(sentence)
# for item in w4:
#     print(item)
# print('-'*20)
# # 词性标注
# import jieba.posseg
# w5 = jieba.posseg.cut(sentence)
# # flag 词性
# # word词语
# for item in w5:
#     print(item.word+'----'+item.flag)
'''
a:形容词
c:连词
d:副词
e:叹词
f:方位词
i:成语
m:数词
n:名词
nr:人名
ns:地名
nt:机构团体
nz:其他专有名词
p:介词
r:代词
t:时间
u:助词
v:动词
vn:动名词
w:标点符号
un:未知词语
'''
# 词典加载
# jieba.load_userdict('路径')

# 更改词频
sentence = '我喜欢上海东方明珠'
w7 = jieba.cut(sentence)
for item in w7:
    print(item)
print('-'*20)
jieba.suggest_freq('上海东方',True)
w8 = jieba.cut(sentence)
for item in w8:
    print(item)

import jieba.analyse
sentence3 = '我喜欢上海东方明珠'
# 提取关键词
tag = jieba.analyse.extract_tags(sentence3,2)
print(tag)
print('-'*20)
# 返回词语的位置
w9 = jieba.tokenize(sentence)
for item in w9:
    print(item)
print('-'*20)
w10 = jieba.tokenize(sentence,mode='search')
for item in w10:
    print(item)

# 分析xueshi的词频
data = open('xueshi.txt','r').read()
tag = jieba.analyse.extract_tags(data,30)
print(tag)