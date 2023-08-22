from get_connection import db_connect
db=db_connect(password="Password@123")
cursor=db.cursor()
query="""create database mobile_shop"""

cursor.execute(query)
