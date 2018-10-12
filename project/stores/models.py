
from project  import db
import uuid
import datetime

from project.accounts.models import UserModel
from project.items.models import ItemModel

class StoresModel(db.Model):
    __tablename__ = 'stores'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(125))
    date_created = db.Column(db.String(125))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name, user_id):
        self.name = name
        self.date_created = str(datetime.datetime.now())
        self.user_id = user_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return { 
                    'name':self.name , 
                    'items':[item.json() for item in self.items.all()],
                    'date_created':self.date_created,
                    'owner': UserModel.find_by_id(self.user_id).username,
                    'id': self.id
                }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter(StoresModel.name.contains(name))

    @classmethod
    def find_by_id(cls, _id):
        return StoresModel.query.get(_id)

    def delete_from_db(self):
        db.session.query(ItemModel).filter(ItemModel.store_id == self.id).delete()

        db.session.delete(self)
        db.session.commit()

        
