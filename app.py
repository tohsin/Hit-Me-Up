from email import message
import os
import uuid as uuid
from ast import parse
import json
import base64
from curses.ascii import US
from distutils.log import debug
from flask import Flask, session
from flask_migrate import Migrate
from models import User, db, Store, Product
from flask_restful import Resource, reqparse, Api , abort
from flask_jwt_extended import jwt_required, create_access_token
from flask_jwt_extended import get_current_user
from models import User, db, Store, Product, Order, OrderItem
from werkzeug.utils import secure_filename
from flask_jwt_extended import  JWTManager
import cloudinary

from cloudinary.uploader import upload

from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify

#Instantiate a flask object 
app = Flask(__name__)
CORS(app)

#Instantiate Api object
api = Api(app)
#Setting the location for the sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
#Adding the configurations for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True 
app.config["JWT_SECRET_KEY"] = "Dese.Decent.Pups.BOOYO0OST"


# cloudinary.config( 
#   cloud_name = "dropshipify", 
#   api_key = "628348882218943", 
#   api_secret = "d6b7p9SwTrJ9g6EgbVPm9ceex-k" 
# )
jwt = JWTManager(app)


#Link the app object to the Movies database 
db.init_app(app)
migrate = Migrate(app, db)

app.app_context().push()
#Create the databases
db.create_all() 

api.add_resource(getWishListItems, '/get-fav-products')


if __name__=='__main__':        
    #Run the applications
    app.run(debug=True) 