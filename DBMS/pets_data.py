import random
from faker import Faker

fake = Faker('en_IN')

animals = ['Dog', 'Cat', 'Bird', 'Rabbit']
breeds = {
    'Dog': ['Labrador', 'Siberian Husky', 'Poodle', 'Doberman'],
    'Cat': ['Persian', 'Ragdoll', 'Siberian'],
    'Bird': ['Parrot', 'Macaw', 'Cockatiel'],
    'Rabbit': ["Holland Lop", "Netherland Dwarf"]
}

# Static prices for each breed
price_mapping = {
    'Labrador': 1500,
    'Siberian Husky': 1800,
    'Poodle': 1600,
    'Doberman': 2000,
    'Persian': 1200,
    'Ragdoll': 1400,
    'Siberian': 1600,
    'Parrot': 1000,
    'Macaw': 2500,
    'Cockatiel': 1500,
    'Holland Lop': 800,
    'Netherland Dwarf': 900
}

# Generate pet data
Data = []
for _ in range(450):  # Adjust the count as needed
    species = random.choice(animals)
    breed = random.choice(breeds[species])

    pet = {
        "Species": species,
        "Pet_Name": fake.first_name(),
        "Breed": breed,
        "Age": random.randint(1, 10),
        "Price": price_mapping.get(breed, 1000)  # Use the price from price_mapping
    }
    Data.append(pet)

    # Optionally print each generated pet (for debugging purposes)
    print(pet)  # This will show the prices before they are added to the table

print("\nGenerated pet data successfully!")
