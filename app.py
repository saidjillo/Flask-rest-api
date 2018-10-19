from  project import app
from flask_jwt import JWT
from flask_restful import Api
from flask import jsonify, render_template

from project.resources.register import RegisterUser
from project.resources.store import Store, StoresList, OneStore, SearchStore, StoreUpdate,StoreDelete
from project.resources.item import Item, Items, ItemUpdate, ItemSearch, OneItem, ItemDelete

from project.accounts.auth import authenticate, identity
  

api = Api(app)

jwt = JWT(app, authenticate, identity) #creates a new endpoint /auth

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/profile')
def my_profile():
    return render_template('multi-dropdown.html')


@app.route('/installation')
def install():
    return render_template('installation.html')



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


from project.stores.views import stores_blueprints
from project.items.views import items_blueprints

app.register_blueprint(stores_blueprints, url_prefix='/query')
app.register_blueprint(items_blueprints, url_prefix='/all')

# @app.errorhandler(404)
# def page_not_found(e):

#     return jsonify({"Error":"Page could not be found"})

    
if __name__ == '__main__':
    app.run()


