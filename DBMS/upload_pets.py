import mysql.connector
from pets_data import Data  # Import the generated pet data

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="vedh@1234",  # Replace with your MySQL password
    database="PETS_DB"  # The database you created
)
cursor = connection.cursor()

# Insert query to add pet data to the table
insert_sql = '''
INSERT INTO Pets (Pet_Name, Species, Breed, Age, Price) 
VALUES (%s, %s, %s, %s, %s)
'''

# Upload each pet's data to the Pets table
for pet in Data:
    val = (pet['Pet_Name'], pet['Species'], pet['Breed'], pet['Age'], pet['Price'])
    cursor.execute(insert_sql, val)

# Commit the changes to the database
connection.commit()
print("Pet data uploaded successfully!")

# Close the database connection
cursor.close()
connection.close()
