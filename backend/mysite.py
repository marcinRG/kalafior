import os
from flask import Flask, render_template, request, send_from_directory, jsonify
from utils.crossdomain import crossdomain
from utils.generate_password import generate_password
from utils.import_text_to_list import import_text_to_list

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'images/favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
@app.route("/home")
def main():
    user_agent = request.headers.get('User-Agent')
    return render_template("main.html", agent=user_agent)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/kubus_puchatek")
def puchatek():
    return render_template('puchalke.html')


@app.route("/kubus_puchatek/data")
@crossdomain(origin='*')
def puchatek_data():
    txt_data = import_text_to_list('./resources/kubus_puchatek.txt')
    response = jsonify(
        author="A. A. MILNE",
        title="'Kubuś Puchatek",
        text=txt_data
    )
    return response


@app.route("/pass_generator/data", methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def password_data():
    password = {}
    if request.method == 'POST':
        password = generate_password(request.json)
    response = jsonify(password)
    return response


@app.route("/pass_generator")
def pass_generator():
    return render_template('pass_generator.html')


if __name__ == '__main__':
    app.run(debug=True)
