import pymysql
connection = pymysql.connect(host='localhost', user='root', password='Admin123', database='vaishnavi')
cursor = connection.cursor()
cursor.execute("insert into college(ID,NAME,COLLEGE,YEAR) values (6,'siddhi','MGM','SYCS')")
connection.commit()
results=cursor.fetchall()
for row in results:
    print(row)
cursor.close()
connection.close()
