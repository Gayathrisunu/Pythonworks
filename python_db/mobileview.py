from get_connection import db_connect

class Mobileview:

    def connect(self):
        db=db_connect(password="Password@123",database="mobile_shop")
        return db


    def get(self):                #retrive all mobile details
        db=self.connect()
        cursor=db.cursor()
        query="""select * from mobiles"""
        cursor.execute(query)
        qs=cursor.fetchall()
        return qs
    
mb=Mobileview()
print(mb.get())
    
       
