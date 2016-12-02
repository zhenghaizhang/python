# import matplotlib.pyplot as pyl
# import pandas as pda
# data = pda.read_excel('data.xls')
# data2 = data.T
# pyl.plot(data2.values[0], data2.values[1])
# pyl.show()

# import pymysql
# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', charset='utf8', db='jd')
# sql = 'select * from auction_info'
# cursor = conn.cursor()
# count = cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
# print()
# conn.close()