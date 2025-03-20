import mysql.connector
import random

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kush1234",
    database="PETS_DB"
)
cursor = connection.cursor()

cursor.execute("SELECT Customer_ID FROM Customers")
customer_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Pet_ID FROM Pets")
pet_ids = [row[0] for row in cursor.fetchall()]

unique_pairs = set()

while len(unique_pairs) < 50:
    customer_id = random.choice(customer_ids)
    pet_id = random.choice(pet_ids)
    
    if (customer_id, pet_id) not in unique_pairs:
        unique_pairs.add((customer_id, pet_id))

sql = """
INSERT INTO Purchase(CustomerID, Customer_Name, PetID, PetName, Species, Amount_Payed)
SELECT c.Customer_ID, c.NAME, p.Pet_ID, p.Pet_Name, p.Species, p.Price
FROM Customers c, Pets p
WHERE c.Customer_ID = %s AND p.Pet_ID = %s
"""

for customer_id, pet_id in unique_pairs:
    cursor.execute(sql, (customer_id, pet_id))

connection.commit()
print("Job Done!")

cursor.close()
connection.close()
