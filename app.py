import os
from flask import Flask,jsonify,request,send_file
from flask_restful import Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

from datetime import timedelta
from resources.user import UserRegister, User
from resources.bilag import BilagList, CreateBilag, UserBilag, Upload, Download

app = Flask(__name__)
app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app,authenticate,identity)

# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

api.add_resource(CreateBilag, '/new_bilag')
api.add_resource(BilagList, '/bilag_list') 
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/users')
api.add_resource(UserBilag, '/user_bilag')
api.add_resource(Upload, '/upload')

api.add_resource(Download, '/download')

app.run(port=5050, debug=True)