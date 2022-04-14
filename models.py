import base64
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import  check_password_hash
from datetime import datetime
import base64
#Instantiating sqlalchemy object
db = SQLAlchemy()


# favourite_shops = db.Table('favourite_shops',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('favourite_shop_id', db.Integer, db.ForeignKey('store.id'))
# )

# class User(db.Model):
#     id = db.Column(db.Integer,primary_key = True)
#     email = db.Column(db.String(150), unique = True)
#     password = db.Column(db.String(150) )
#     first_name = db.Column(db.String(150))
#     last_name = db.Column(db.String(150))
#     is_retailer = db.Column(db.Boolean(),default= False)
#     mailing_address = db.Column(db.String(150))
#     city = db.Column(db.String(150) )
#     state = db.Column(db.String(150) )
#     zip_ = db.Column(db.String(150) )
#     mailing_phone_number = db.Column(db.String(150))
#     store = db.relationship("Store", uselist=False, backref='user')
#     orders = db.relationship("Order", backref='user',lazy='dynamic')
#     favoutite_stores = db.relationship("Store",secondary = favourite_shops)
#     favoutite_products = db.relationship("Product", secondary = favourite_products, backref ='products')
#     favoutite_niche = db.relationship("Niche",secondary = favourite_niche)
#     def __repr__(self):
#         return '<User {}>'.format(self.email)
#     # def set_password(self, password):
#     #     self.password_hash = generate_password_hash(password, method='sha256')

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#     def json(self):        
#         return {'id': self.id, 
#                 'email': self.email, 
#                 'first_name': self.first_name, 
#                 'last_name': self.last_name, 
#                 'is_retailer': self.is_retailer,
#                 'mailing_address': self.mailing_address,
#                 'city': self.city,
#                 'state': self.state,
#                 'zip': self.zip_,
#                 'store_id':self.store.id if self.store else None,
#                 'mailing_phone_number': self.mailing_phone_number}        
#     def save_to(self):        
#         db.session.add(self)        
#         db.session.commit()
#     def delete_(self):        
#         db.session.delete(self)        
#         db.session.commit()
    
    