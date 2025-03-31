import mysql.connector
from products_data import product_data

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vedh@1234",
    database="PETS_DB"
)
cursor = connection.cursor()

sql = "INSERT INTO Products(Product_Name, Category, Price, Stock) VALUES (%s, %s, %s, %s)"

cursor.executemany(sql, product_data)
connection.commit()
print("Products Uploaded Successfully!")

cursor.close()
connection.close()
