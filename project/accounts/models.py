# project/accounts/models.py
from project import db
from werkzeug.security import check_password_hash, generate_password_hash
import uuid

# from project.items.models import ItemModel
# from project.stores.models import StoresModel
 
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(25))
    lastname = db.Column(db.String(25))
    email = db.Column(db.String(81), unique=True)
    username = db.Column(db.String(25), unique=True)
    password_hash = db.Column(db.String(81), unique=True) 

    stores = db.relationship('StoresModel', backref='stores', lazy='dynamic')
    cart = db.relationship('Cart', backref='carts', lazy='dynamic')
    notifictions = db.relationship('Notifications', backref='notifications', lazy='dynamic')
    amount = db.Column(db.Integer)

 

    def __init__(self, firstname, lastname, email, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password_hash = password
        

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def save_user_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def save_amount_to_db(amount, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if user:
            user.amount += amount
            db.session.add(user)
            db.session.commit()


    @classmethod
    def find_by_username(cls, username):
        return UserModel.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, user_id):
        return UserModel.query.filter_by(id=user_id).first()

    def json(self):
        return {
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email
        }


class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(81))
    items = db.relationship('ItemModel', backref='items', lazy='dynamic')
 
    price = db.Column(db.Integer)
    date_added = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, item_id, price, date_added, user_id):
        self.name = name
        self.item_id = item_id
        self.price = price
        self.date_added = date_added
        self.user_id = user_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            'name':self.name,
            'item_id':self.item_id,
            'price': self.price,
            'date_ordered': self.date_added
        }


class Notifications(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    date_created = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, message, date_created, user_id):
        self.message = message
        self.date_created = date_created
        self.user_id = user_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            'message':self.message,
            'user_id': self.user_id,
            'date_created': self.date_created
        }
    
