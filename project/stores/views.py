from flask import Blueprint , render_template

stores_blueprints = Blueprint('query', __name__, template_folder='templates/stores')




@stores_blueprints.route('/stores')
def store_queries():

    return render_template('stores.html')