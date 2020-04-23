import pymysql

user = input("username:")
pwd = input("password:")

conn = pymysql.connect(host="192.168.5.17",user='root',password='Admin-12345',database='pythonStudy')
cursor = conn.cursor()
sql = "select * from userinfo where username=%s and password=%s"

cursor.execute(sql,[user,pwd])
result = cursor.fetchone()

cursor.close()
conn.close()

if result:
    print('登陆成功')
else:
    print('登录失败')
