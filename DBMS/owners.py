import random
from faker import Faker
fake=Faker('en_IN')

data=[]
for _ in range(51):
    name = fake.name().title()
    num = random.randint(100,1000)
    email = f'{name.split()[0].lower()}{num}@gmail.com'
    details = {
        'name' : name,
        'num' : fake.phone_number(),
        'email' : email
    }
    data.append(details)
    print(details)
    print('-'*40)
    