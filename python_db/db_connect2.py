import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Password@123",
    database="animal"
)
cursor=db.cursor()
#create a table pets
#id age weight breed image
query="""create table pets
         (id int auto_increment primary key, 
         age int not null,
         gender varchar(100) not null,breed varchar(200) not null,
         location varchar(200) not null,
         price int not null)
         """
cursor.execute(query)
