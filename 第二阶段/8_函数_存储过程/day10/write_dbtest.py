"""
写入数据库示例
"""

import pymysql

# 链接数据库
db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user="root",
                     password='123456',
                     database="singer",
                     charset="utf8")

# 创建游标 (调用sql语句,获取执行结果)
cur = db.cursor()

# 写数据操作
try:
    # sql = "update cls set score=70 where name='Lily';"
    # cur.execute(sql)

    sql = "insert into dict (word,meaning) values (%s,%s);"
    cur.execute(sql,["zephyr","n.  point in the heavens directly above an observer"])
    db.commit()   # 提交
except Exception as e:
    print(e)
    db.rollback() # 回滚



# 关闭游标和数据库
cur.close()
db.close()