import mysql.connector
import random
from datetime import datetime, timedelta

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kush1234",
    database="PETS_DB"
)
cursor = connection.cursor()

# cursor.execute("SELECT Customer_ID FROM Customers")
# customer_ids = [row[0] for row in cursor.fetchall()]

# cursor.execute("SELECT Pet_ID FROM Pets")
# pet_ids = [row[0] for row in cursor.fetchall()]

# unique_pairs = set()

# while len(unique_pairs) < 50:
#     customer_id = random.choice(customer_ids)
#     pet_id = random.choice(pet_ids)
    
#     if (customer_id, pet_id) not in unique_pairs:
#         unique_pairs.add((customer_id, pet_id))
        

def genDateTime(start_date, end_date, total) :
    randomDates = [ ]
    start = start_date.timestamp()
    end = end_date.timestamp()
    
    for _ in range(total):
        random_timestamp = random.uniform(start, end)
        random_dates = datetime.fromtimestamp(random_timestamp)
        randomDates.append(random_dates)
        
    return randomDates

start = datetime(2024,1,1)
end = datetime(2025,4,1)

random_dates = genDateTime(start, end, 50)
for date in random_dates:
    print(date.strftime("%Y-%m-%d %H:%M:%S"))

payment_methods = ["Cash", "Credit Card", "Debit Card", "UPI"]
sql = '''
UPDATE Purchase 
SET Payment_Method = %s, Payment_Date_and_Time = %s
WHERE Transaction_ID = %s
'''
row_ids = list(range(1, 51))  

for i, dates in enumerate(random_dates[:50]):  
    payment = random.choice(payment_methods)
    val = (payment, dates, row_ids[i])  
    cursor.execute(sql, val)
    
    
# sql = """
# INSERT INTO Purchase(CustomerID, Customer_Name, PetID, PetName, Species, Amount_Payed)
# SELECT c.Customer_ID, c.NAME, p.Pet_ID, p.Pet_Name, p.Species, p.Price
# FROM Customers c, Pets p
# WHERE c.Customer_ID = %s AND p.Pet_ID = %s
# """

# for customer_id, pet_id in unique_pairs:
#     cursor.execute(sql, (customer_id, pet_id))

connection.commit()
print("Job Done!")

cursor.close()
connection.close()
