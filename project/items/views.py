from flask import Blueprint, render_template


items_blueprints = Blueprint('all', __name__, template_folder='templates/items')


@items_blueprints.route('/items')
def item_query():
    return render_template('items.html')


@items_blueprints.route('/items/search')
def item_search():
    return render_template('search_items.html')