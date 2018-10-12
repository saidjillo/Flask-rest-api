# imports
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from project.items.models import ItemModel

class Item(Resource):
    """
    This api endpoint create a new item with the specified name

    """
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required=True,
        help = 'This field cannot be left blank'
    )

    parser.add_argument('store_id',
        type = int,
        required=True,
        help = 'Every item needs a store id'
    )

 
    def post(self, name):

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.save_to_db()
        except:
            return {'message':'An error occured while saving the item into the database'}, 500 #internal server error

        
        return item.json(), 201  # item was created successfully



class Items(Resource):

    def get(self):
        # return {"items": [item.json() for item in ItemModel.query.all()] }, 200 # list comprehension
        return {"items": list(map(lambda x: x.json(), ItemModel.query.all())) }, 200  # lambda


class OneItem(Resource):

        def get(self, _id): 
            item = ItemModel.find_by_id(_id)

            if item:
                return item.json(),200
            return {'message':'item was not found'}, 404


class ItemDelete(Resource):

    def delete(self,_id):

        item = ItemModel.find_by_id(_id)
        if item:
            item.delete_from_db(_id)

        return {"message":"Item deleted"}, 201


class ItemUpdate(Resource):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
            type = float,
            required=True,
            help = 'This field cannot be left blank'
        )

        parser.add_argument('store_id',
            type = int,
            required=True,
            help = 'Every item needs a store id'
        )

        parser.add_argument('name',
            type = str,
            required=True,
            help = 'Every item must have a name'
        )

        def put(self, _id):      
            data = ItemUpdate.parser.parse_args()
            item = ItemModel.find_by_id(_id)

            if item is None:

                item = ItemModel(data['name'], data['price'], data['store_id'])

            else:
                item.price = data['price']
                item.name = data['name']

            item.save_to_db()

            return item.json() , 201


class ItemSearch(Resource):

    def get(self, name):
        items = ItemModel.find_by_name(name)

        item_list = [item.name for item in items]
        
        #check array length
        if len(item_list) > 0:
            for item in items:

                return {'items': {
                        'name':item.name,
                        'id':item.id
                    }
                }

        else:
            return {'message':'No items matches {}'.format(name)}



