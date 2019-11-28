# print语句的多种写法

# 一般写法
print('Hello %s!' % ('Baoshan',))
# 再精进一点
print('Hello %(name)s!' % {'name':'Baoshan'})
# 参数比较多的情况下使用
value = {'great':'Hello world', 'language':'Python'}
print('%(great)s from %(language)s.' % value)
# 更具有Pythonic风格的代码如下
print('{great} from {language}.'.format(great = 'Hello World', language = 'Python'))


# str.format()方法非常清晰地表明了这条语句的意图，而且模板的使用也减少了许多不必要的字符，使可读性得到了很大的提升。事实上，str.format()也成了Python最为推荐的字符串格式化方法，当然也是最Pythonic的。
