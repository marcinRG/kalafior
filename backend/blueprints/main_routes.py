from flask import Blueprint, send_from_directory

main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'images/favicon.ico', mimetype='image/vnd.microsoft.icon')
