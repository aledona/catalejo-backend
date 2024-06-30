from flask import jsonify, request
from app.models import User, Country
import datetime

def get_all_countries():
    countries = Country.get_all()
    return jsonify([country.serialize() for country in countries])

def create_user():
    data = request.json
    new_user = User(None,data['firstname'],data['lastname'],data['genre'],data['email'],
                    data['password'],data['birthdate'],data['country'],data['lastlogin'])
    new_user.CreateUser()
    response = {'message':'El usuario fue creado con exito'}
    return jsonify(response) , 201

def login_user():
    data = request.json
    user = User.get_by_email(data['email'])
    if user!=None:            
        if user.password == data['password']:     
            userlogin = User.get_by_id(user.id)   
            return jsonify(userlogin.serialize())
        else:
            return jsonify({'message': 'User not found'}), 404
    else:
      return jsonify({'message': 'User not found'}), 404  

def update_lastlogin(id):
    user = User.get_by_id(id)
    if not user:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    user.lastlogin = datetime.datetime.now()
    user.saveLastLogin()
    return jsonify({'message': 'Usuario actualizado con éxito'})

def delete_user(id):
    user = User.get_by_id(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user.delete()
    return jsonify({'message': 'User deleted successfully'})
