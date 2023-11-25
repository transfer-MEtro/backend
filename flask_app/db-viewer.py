import pymysql
import pandas as pd

db = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                     passwd='root123!', db='pbj_db', charset='utf8')
cursor = db.cursor()

sql = '''SELECT * FROM pbj_db.Score;'''
cursor.execute(sql)

result = cursor.fetchall()

db.close()

a = pd.DataFrame(result)

print(a)
