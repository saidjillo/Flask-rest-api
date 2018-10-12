from flask_restful import Resource, reqparse
from project.stores.models import StoresModel
from project.items.models import ItemModel


class Store(Resource):
    """
    This api create a new store with specified name in the url
    """
    parser = reqparse.RequestParser()
 
    parser.add_argument('user_id',
       type=int,
       required=True,
       help='This field cannot be left blank'
    )
  
    def post(self, name):
        data = Store.parser.parse_args()
        store = StoresModel(name, data['user_id'])

        try:
            store.save_to_db(), 201
        except:
            return {'message':'An error occured while creating the store'}, 500

        return store.json() , 201



class StoresList(Resource):
    """
    This api returns a list of all stores from the database
    """

    def get(self):
        return {'stores':  [store.json() for store in StoresModel.query.all()] } , 200


class OneStore(Resource):
    """
       This api returns the specified store and all its items in the store
       It returns  list of items from the store
    """

    def get(self, _id):
        store = StoresModel.find_by_id(_id)

        # check if the store was found
        if store:
            return store.json(), 200
        else:
            return {'message': 'Store with that id {} was not found'.format(_id)}, 404


class SearchStore(Resource):

    """
    This api searches the database for stores by the specified  in the url

    """
    def get(self, name):
        stores = StoresModel.find_by_name(name)

        storesList = [store.name for store in stores]
        if len(storesList) > 0:
            for store in stores:

                return {
                    'stores': {
                        'name': store.name,
                        'date_created': store.date_created
                    }
                }

        else:
            return {'message': 'No store matches {}'.format(name)}


class StoreUpdate(Resource):
    """
    This api updates the store. First it check the existense of the store , if the store is 
    available, the store is updated with the new credentials i.e the store name. Otherwise a new store is created with the 
    provided credentials

    """
    parser = reqparse.RequestParser()
    parser.add_argument('name',
       type=str,
       required=True,
       help='This field cannot be left blank'
    )

    parser.add_argument('user_id',
       type=int,
       required=True,
       help='This field cannot be left blank'
    )

    def put(self, _id):
        store = StoresModel.find_by_id(_id)
        data = StoreUpdate.parser.parse_args()

        if store is None:

            store = StoresModel(data['name'], data['user_id'])
        else:
            store.name = data['name']
      
        store.save_to_db()

        return store.json(), 201


class StoreDelete(Resource):
    """

    This delete the specified store and its related items from the database

    """

    def delete(self, _id):
        # create store instance
        store = StoresModel.find_by_id(_id)

        # check if the store exists
        if store is None:
            return {'message': 'The store has been deleted successfully'}
        else:
            store.delete_from_db()

            return {'message':'The store has been deleted successfully'}