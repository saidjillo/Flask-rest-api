from  project import app
from flask_jwt import JWT
from flask_restful import Api
from flask import jsonify

from project.resources.register import RegisterUser
from project.resources.store import Store, StoresList, OneStore, SearchStore, StoreUpdate,StoreDelete
from project.resources.item import Item, Items, ItemUpdate, ItemSearch, OneItem, ItemDelete

from project.accounts.auth import authenticate, identity
  

api = Api(app)

jwt = JWT(app, authenticate, identity) #creates a new endpoint /auth

api.add_resource(RegisterUser, '/register')

api.add_resource(StoresList, '/stores')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(OneStore, '/store/<int:_id>')
api.add_resource(SearchStore, '/stores/<string:name>')
api.add_resource(StoreUpdate, '/store/<int:_id>/update')
api.add_resource(StoreDelete, '/store/<int:_id>/delete')

api.add_resource(Items,'/items')
api.add_resource(OneItem, '/search/<int:_id>')
api.add_resource(ItemDelete, '/delete/<int:_id>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemUpdate, '/item/<int:_id>')
api.add_resource(ItemSearch, '/item/search/<string:name>')



@app.errorhandler(404)
def page_not_found(e):

    return jsonify({"Error":"Page could not be found"})


    
if __name__ == '__main__':
    app.run()


