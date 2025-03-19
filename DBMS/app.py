from flask import Flask, request, jsonify
from database import app, db
from models import Pet  # Import models

# Add a new pet
@app.route('/pets', methods=['POST'])
def add_pet():
    data = request.get_json()
    new_pet = Pet(name=data['name'], species=data['species'], age=data['age'], price=data['price'])
    db.session.add(new_pet)
    db.session.commit()
    return jsonify({"message": "Pet added successfully!"}), 201

# Get all pets
@app.route('/pets', methods=['GET'])
def view_pets():
    pets = Pet.query.all()
    return jsonify([{"id": pet.id, "name": pet.name, "species": pet.species, "age": pet.age, "price": pet.price} for pet in pets])

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
