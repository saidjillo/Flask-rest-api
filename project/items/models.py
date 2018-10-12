# from project.stores.models import StoresModel
from project import db
import datetime
import uuid

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(81))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))

    

    likes = db.Column(db.Integer)
    date_created = db.Column(db.String)


    store = db.relationship('StoresModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
        self.date_created = str(datetime.datetime.now())

    def json(self):
        return {'name':self.name, 'price':self.price}


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self, _id):
        item = ItemModel.query.get(_id)

        db.session.delete(item)
        db.session.commit()

    def update_item_name(self, item_id, name):
        # get item object from database
        item = ItemModel.query.get(item_id)

        # set the new item name
        item.name = name

        # save changes to databse
        db.session.add(item)
        db.session.commit()

    # def update_item_name(self, item_id, price):
    #     # get item object from database
    #     item = ItemModel.query.get(item_id)

    #     # set the new item name
    #     item.price = price

    #     # save changes to databse
    #     db.session.add(item)
    #     db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter(ItemModel.name.contains(name))
        # Model.query.filter(Model.columnName.contains('sub_string'))

    @classmethod
    def find_by_id(cls, _id):
        return ItemModel.query.get(_id)
         