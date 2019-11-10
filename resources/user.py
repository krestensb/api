import sqlite3
from flask_restful import Resource
from flask import request
from flask_jwt import jwt_required

from models.user import UserModel


class User(Resource):
	@jwt_required()
	def get(self):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		query = "SELECT * FROM users"

		result = cursor.execute(query)
		row = result.fetchall()
		connection.close()

		return {'users': row}


class UserRegister(Resource):

	def post(self):
		data = request.get_json()
		if data['username'] == 'admin':
			return {'message': 'There can only be one admin user admin user!'}, 403

		if UserModel.find_by_username(data['username']):
			return {'message': 'User allready exists!'}, 400
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		insert_query = "INSERT INTO users VALUES (NULL,?,?)"

		cursor.execute(insert_query,(data['username'],data['password']))
		
		connection.commit()
		connection.close()

		return {'message': 'User created!'}