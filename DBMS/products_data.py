import random
from faker import Faker
fake = Faker()

products = [
    {"Product_Name": "Dog Food", "Category": "Food", "Price": 500},
    {"Product_Name": "Cat Food", "Category": "Food", "Price": 400},
    {"Product_Name": "Bird Cage", "Category": "Accessories", "Price": 1200},
    {"Product_Name": "Rabbit Hutch", "Category": "Accessories", "Price": 2000},
    {"Product_Name": "Dog Belt", "Category": "Belt", "Price": 300},
]

product_data = []
for _ in range(50):
    product = random.choice(products)
    stock = random.randint(5, 50)  # Random stock value
    product_data.append((product["Product_Name"], product["Category"], product["Price"], stock))

print(product_data)
