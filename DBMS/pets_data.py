import random
from faker import Faker
fake=Faker('en_IN')

animals= ['Dog','Cat','Bird','Rabbit']
breeds = {
    'Dog':['Labrador','Siberian Husky','Poodle','Doberman'],
    'Cat':['Persian','Ragdoll','Siberian'],
    'Bird':['Parrot','Macaw','Cockatiel',],
    'Rabbit':["Holland Lop", "Netherland Dwarf"]
}
Data = [ ]
for _ in range(50):
    species = random.choice(animals)
    breed = random.choice(breeds[species])
    
    pet = {
        "Species": species,
        "Pet_Name": fake.first_name(),
        "Breed": breed,
        "Age": random.randint(1, 10)
    }
    Data.append(pet)
    print(pet)
print('\n')