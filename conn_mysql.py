import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="python"
)

myConn = conn.cursor()

myConn.execute("select * from users")

users = myConn.fetchall()
for user in users:
    print(user)
