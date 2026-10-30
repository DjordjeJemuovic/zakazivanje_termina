import pymysql

connection = pymysql.connect(
    host='localhost',
     user='root',
     password='12345678',
     db='termino',
     cursorclass=pymysql.cursors.DictCursor
)
if connection.open:
    print("Connected :D")

else:
    print("Connection failed")