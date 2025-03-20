import mysql.connector
from pets_data import Data

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kush1234",
    database="PETS_DB"
)
cursor = connection.cursor()
sql = 'INSERT INTO Pets(Species, Pet_Name, Breed, Age) VALUES (%s,%s,%s,%s)'

for pet in Data:
    val = (pet['Species'],pet['Pet_Name'],pet['Breed'],int(pet['Age']))
    cursor.execute(sql,val)
connection.commit()
print('Job Done!')

cursor.close()
connection.close()
