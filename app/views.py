from flask import jsonify, request
from app.models import User, Country
import datetime

def index():
    response = {'message':'Hola Mundo API-REST Flask 🐍'}
    return jsonify(response)

def get_all_countries():
    countries = Country.get_all()
    return jsonify([country.serialize() for country in countries])

def create_user():
    data = request.json
    new_user = User(None,data['firstname'],data['lastname'],data['genre'],data['email'],
                    data['passsword'],data['birthday'],data['country'],data['lastlogin'])
    new_user.CreateUser()
    response = {'message':'El usuario fue creado con exito'}
    return jsonify(response) , 201

def update_lastlogin(id):
    user = User.get_by_id(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    data = request.json
    user.lastlogin = datetime.datetime.now()
    user.saveLastLogin()
    return jsonify({'message': 'User updated successfully'})

def delete_user(id):
    user = User.get_by_id(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user.delete()
    return jsonify({'message': 'User deleted successfully'})
