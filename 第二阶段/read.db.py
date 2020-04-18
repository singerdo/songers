import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="singer",
                     charset="utf8")

cur=db.cursor()
name="Emma"#为什么行不通，也想不明白（我在脑袋里确认%s的使用规则，确认无误后就束手无策了）
sql="select name,age,score from class_2 where name=%s or score>%s";
cur.execute(sql,[name,85])
#第一种读取方法
# for i in cur:
#     print(i)
#第二种方法
#fetchmany、fetchall获取的是嵌套元祖
# fetchone获取的是元祖,如果没有结果返回none
one=cur.fetchone()
print(one)

cur.close()
db.close()