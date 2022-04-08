from flask import Blueprint, render_template, jsonify, request
from utils.generate_password import generate_password

password_generator = Blueprint('password_generator', __name__)


@password_generator.route("/pass_generator/data", methods=['POST', 'OPTIONS'])
def password_data():
    password = {}
    if request.method == 'POST':
        password = generate_password(request.json)
    response = jsonify(password)
    return response


@password_generator.route("/pass_generator")
def pass_generator():
    return render_template('pass_generator.html')
