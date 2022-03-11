import os
from flask import Flask, render_template, request, send_from_directory, jsonify, redirect, url_for, g, session

from cms.load_cms_lists import load_cms_lists
from cms.login_admin import login_admin
from utils.crossdomain import crossdomain
from utils.generate_password import generate_password
from utils.import_text_to_list import import_text_to_list
from cms.cms_settings_file import cms_settings_file
from cms.cms_settings_file import cms_admin

app = Flask(__name__)
app.secret_key = 'NFcT&jCOn#ekRB~qyh9gSAso*l2+pXYUwDHt!PI5'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'images/favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/", methods=['GET', 'POST', 'OPTIONS'])
def main():
    page_data = load_cms_lists(cms_settings_file)
    sections = page_data.get('sections')
    menu_items = list(filter(lambda x: x.get('show_on_menu'), sections))
    sub_pages = list(filter(lambda x: x.get('create_section'), sections))
    html_elem = '<div><p>content</p><p>Something else</p></div>'
    return render_template("index.html", menu_items=menu_items, sub_pages=sub_pages, elem_active=html_elem)


@app.route("/admin", methods=['GET', 'POST', 'OPTIONS'])
def admin():
    if request.method == 'POST':
        print('post')
        post_data = request.form.to_dict()
        if post_data.get('form_type') == 'login_form':
            logged_in = login_admin(post_data, cms_admin)
            if logged_in:
                session['login'] = post_data.get('login')
                session['logged_in'] = logged_in
                session['user_role'] = 'admin'
                return redirect('admin')

    if request.method == 'GET':
        get_parameters = request.args.to_dict()
        print(request.path)
        if get_parameters.get('logout') == 'ok':
            session.pop('login')
            session.pop('logged_in')
            session.pop('user_role')
            return redirect('admin')

    return render_template("admin.html", logged_in=session.get('logged_in'), login=session.get('login'),
                           user_role=session.get('user_role'))


@app.route("/data/slider_items")
@crossdomain(origin='*')
def slider_items():
    page_data = load_cms_lists(cms_settings_file)
    sections = page_data.get('sections')
    items = list(filter(lambda x: x.get('show_on_slide'), sections))
    return jsonify(items)


@app.route("/kubus_puchatek")
def puchatek():
    return render_template('puchalke.html')


@app.route("/kubus_puchatek/data")
@crossdomain(origin='*')
def puchatek_data():
    txt_data = import_text_to_list('resources/kubus_puchatek/kubus_puchatek.txt')
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
