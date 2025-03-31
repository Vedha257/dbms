import mysql.connector
from products_data import product_data  # Assuming product data is in this file

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vedh@1234",
    database="PETS_DB"
)
cursor = connection.cursor(buffered=True)

for product in product_data:
    product_name, category, price, stock = product

    # ✅ Ensure uniqueness by checking if product exists
    cursor.execute("SELECT Product_ID, Stock FROM Products WHERE Product_Name = %s AND Price = %s", (product_name, price))
    existing_product = cursor.fetchone()

    if existing_product:
        product_id, existing_stock = existing_product
        new_stock = existing_stock + stock
        cursor.execute("UPDATE Products SET Stock = %s WHERE Product_ID = %s", (new_stock, product_id))
    else:
        cursor.execute("INSERT INTO Products (Product_Name, Category, Price, Stock) VALUES (%s, %s, %s, %s)",
                       (product_name, category, price, stock))

connection.commit()
print("✅ Products uploaded successfully without duplicates!")

cursor.close()
connection.close()
