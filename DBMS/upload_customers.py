import mysql.connector
from Customers import data

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vedh@1234",
    database="PETS_DB"
)
cursor = connection.cursor()
sql = 'INSERT INTO Customers(NAME, CONTACT, EMAIL) VALUES (%s,%s,%s)'

for x in data:
    val = (x['name'],x['num'],x['email'])
    cursor.execute(sql,val)
    
connection.commit()
print('Job Done!')
cursor.close()
connection.close()