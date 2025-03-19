import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PETS_DB"
)
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS PETS_DB;")
cursor.execute('SHOW DATABASES;')
for db in cursor:
    print(db)
    
def add_pets(species, name, breed, age):
    sql = 'INSERT INTO Pets(Species, Pet_Name, Breed, Age) VALUES(%s,%s,%s,%s);'
    val = (species, name, breed, age)
    cursor.execute(sql,val)
    connection.commit()
# add_pets('Dog','Ghost','Husky',5)

def get_pets():
    cursor.execute("SELECT*FROM Pets;")
    for pets in cursor.fetchall():
        print(pets)
get_pets()
print('\n\n')

def delete_pet():
    get_pets() 

    pet = input("Enter the ID(s) of the pet(s) you'd like to delete (separated by spaces): ")
    pet_id = tuple(map(int, pet.split())) 

    if not pet_id:  
        print("No valid IDs entered.")
        return

    sql = f"DELETE FROM pets WHERE id IN ({', '.join(['%s'] * len(pet_id))})"

    cursor.execute(sql,pet_id)
    connection.commit()
    print("Pet(s) deleted successfully!")

# delete_pet()
# get_pets() 

    