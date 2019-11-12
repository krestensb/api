import os
import sqlite3
from flask_restful import Resource
from flask import request,send_file
from flask_jwt import jwt_required, current_identity
from werkzeug.utils import secure_filename

from models.bilag import BilagModel

class UserBilag(Resource):
	@jwt_required()
	def get(self):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		query = f"SELECT * FROM bilag WHERE username = '{current_identity.username}'"

		result = cursor.execute(query)
		row = result.fetchall()
		connection.close()

		return {'bilag': row}

class BilagList(Resource):
    @jwt_required()
    def get(self):
        if current_identity.username != 'admin':
            return {'message': 'access limited to admin user!'}, 403
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM bilag"

        result = cursor.execute(query)
        row = result.fetchall()
        connection.close()

        return {'bilag': row}


class CreateBilag(Resource):
	@jwt_required()
	def post(self):
		data = request.get_json()

		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		insert_query = "INSERT INTO bilag VALUES (NULL,?,?,?)"

		cursor.execute(insert_query,(data['description'], data['price'], current_identity.username))
		
		connection.commit()
		connection.close()

		return {'message': 'Bilag created!'}


class Upload(Resource):
    @jwt_required()
    def post(self):
        new_file = request.files['file']
        file_name = secure_filename(new_file.filename)
        new_file.save(os.path.join('uploads', file_name))
        return {'message': new_file.filename}

class Download(Resource):
    @jwt_required()
    def get(self):
        try:
            return send_file('uploads/faktura-2019066.pdf')
        except:
            return {'message':'File not found!'}, 404

class Test(Resource):
    def get(self):
        try:
            return {'message': 'The test is succesfull!'}, 200
        except:
            return {'message': 'Error loading content!'}, 404