import mysql.connector
import random
from datetime import datetime

def generate_purchases():
    # Database connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="vedh@1234",
        database="PETS_DB"
    )
    cursor = conn.cursor(dictionary=True)

    try:
        # Fetch required data
        cursor.execute("SELECT Customer_ID, Name FROM Customers")
        customers = cursor.fetchall()

        cursor.execute("SELECT Pet_ID, Pet_Name, Species, Price FROM Pets WHERE Price > 0")
        pets = cursor.fetchall()

        cursor.execute("SELECT Product_ID, Product_Name, Price, Stock FROM Products WHERE Stock > 0")
        products = {row['Product_ID']: row for row in cursor.fetchall()}

        # Generate purchases
        payment_methods = ["Cash", "Credit Card", "Debit Card", "UPI"]
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2025, 4, 1)

        for _ in range(50):  # Generate 50 purchases
            # Select random customer and payment method
            customer = random.choice(customers)
            payment_method = random.choice(payment_methods)
            date = datetime.fromtimestamp(random.uniform(start_date.timestamp(), end_date.timestamp()))

            # Initialize purchase details
            pet_id = pet_name = species = None
            product_id = product_name = None
            quantity = 0
            amount = 0.0

            # Process pet purchase (50% chance)
            if random.choice([True, False]) and pets:
                pet = random.choice(pets)
                pet_id, pet_name, species, pet_price = pet['Pet_ID'], pet['Pet_Name'], pet['Species'], float(pet['Price'])
                amount += pet_price

            # Process product purchase (50% chance)
            if random.random() < 0.5 and products:
                available_products = [pid for pid in products if products[pid]['Stock'] > 0]
                if available_products:
                    product_id = random.choice(available_products)
                    product = products[product_id]
                    quantity = random.randint(1, min(5, product['Stock']))
                    amount += float(product['Price']) * quantity
                    product_name = product['Product_Name']

                    # Update product stock
                    cursor.execute(
                        "UPDATE Products SET Stock = Stock - %s WHERE Product_ID = %s",
                        (quantity, product_id)
                    )

            # Skip if nothing purchased
            if amount == 0:
                continue

            # Insert purchase record
            cursor.execute("""
                INSERT INTO Purchase (
                    CustomerID, Customer_Name,
                    PetID, PetName, Species,
                    ProductID, ProductName, Quantity,
                    Amount_Payed, Payment_Method, Payment_Date_and_Time
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                customer['Customer_ID'],
                customer['Name'],
                pet_id,
                pet_name,
                species,
                product_id,
                product_name,
                quantity if product_id else (1 if pet_id else 0),
                amount,
                payment_method,
                date
            ))

        conn.commit()

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    generate_purchases()