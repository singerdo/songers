import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="singer",
                     charset="utf8")
# try:
cur = db.cursor()
f=open("test.txt")
try:
    for i in f:
        l=i.split(" ")
        m=" ".join(l[1:]).strip()
        # print(type(l[0]))
        # print(type(m))
        sql="insert into dict (word,meaning) values (%s,%s);"
        cur.execute(sql,[l[0],m])
    db.commit()
    f.close()

except:
    print("shibai")
    db.rollback()
cur.close()
db.close()