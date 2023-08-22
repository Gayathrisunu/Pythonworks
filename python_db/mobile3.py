from get_connection import db_connect

db=db_connect(password="Password@123",database="mobile_shop")

cursor=db.cursor()
query="""insert into mobiles(name,spec,price) values('one plus 12','fantastic',78000)"""

cursor.execute(query)
db.commit()