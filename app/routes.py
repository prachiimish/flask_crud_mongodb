from flask import Blueprint, jsonify, request
from app import mongo

user_routes = Blueprint('user_routes', __name__)

# GET /users - List all users
@user_routes.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()  # Retrieve all users from the database
    users_list = []
    for user in users:
        user.pop('_id', None)  
        users_list.append(user)
    return jsonify(users_list), 200

# GET /users/<id> - Get a user by ID
@user_routes.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({"id": id})  # Find user by id
    if user:
        user.pop('_id', None)  
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

# POST /users - Create a new user
@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()  
    if 'id' not in data or 'name' not in data or 'email' not in data or 'password' not in data:
        return jsonify({"message": "Missing required fields"}), 400

    # handle duplication
    existing_user = mongo.db.users.find_one({"id": data['id']})
    if existing_user:
        return jsonify({"message": "A user with this ID already exists"}), 400

    
    new_user = {
        "id": data['id'],
        "name": data['name'],
        "email": data['email'],
        "password": data['password']
    }

    
    mongo.db.users.insert_one(new_user)

   
    new_user.pop('_id', None)

    return jsonify(new_user), 201

# PUT /users/<id> - Update a user by ID
@user_routes.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json() 
    updated_user = {}

    if 'name' in data:
        updated_user['name'] = data['name']
    if 'email' in data:
        updated_user['email'] = data['email']
    if 'password' in data:
        updated_user['password'] = data['password']

    if not updated_user:
        return jsonify({"message": "No fields to update"}), 400

    # Update the user in the database
    result = mongo.db.users.update_one({"id": id}, {"$set": updated_user})
    if result.matched_count > 0:
        updated_user['id'] = id  # Add the ID to the updated user data
        return jsonify(updated_user), 200
    return jsonify({"message": "User not found"}), 404

# DELETE /users/<id> - Delete a user by ID
@user_routes.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    # Delete the user from the database
    result = mongo.db.users.delete_one({"id": id})
    if result.deleted_count > 0:
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "User not found"}), 404
