import mysql.connector as sql

db = sql.connect (
    host = "localhost",
    user = "root",
    passwd = "1111",
    database = "mysql",
)

cursor = db.cursor()

query = "select * from table"
cursor.execute(query)
cursor.close()