import os
from flask import Flask, render_template, request, send_from_directory, jsonify, redirect, url_for, g, session

from cms.CMS import CMS
from cms.load_cms_lists import load_cms_lists
from cms.login_admin import login_admin
from utils.crossdomain import crossdomain
from utils.generate_password import generate_password
from utils.import_text_to_list import import_text_to_list
from cms.cms_settings_file import cms_settings_file, cms_settings_file_new
from cms.cms_settings_file import cms_admin

app = Flask(__name__)
app.secret_key = 'NFcT&jCOn#ekRB~qyh9gSAso*l2+pXYUwDHt!PI5'

cms = CMS(os.getcwd(), cms_admin, cms_settings_file_new)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'images/favicon.ico', mimetype='image/vnd.microsoft.icon')


#
#
# @app.route("/", methods=['GET', 'POST', 'OPTIONS'])
# def main():
#     page_data = load_cms_lists(cms_settings_file)
#     sections = page_data.get('sections')
#     print(page_data)
#     menu_items = list(filter(lambda x: x.get('show_on_menu'), sections))
#     sub_pages = list(filter(lambda x: x.get('create_section'), sections))
#     html_elem = '<div><p>content</p><p>Something else</p></div>'
#     return render_template("index.html", menu_items=menu_items, sub_pages=sub_pages, elem_active=html_elem)


@app.route("/admin", methods=['GET', 'POST', 'OPTIONS'])
def admin():
    section = {
        "id": "new_section",
        "short_name": "eło eło",
        "long_name": "Cośtam cośtam ele elo",
        "show_on_slide": True,
        "show_on_menu": True,
        "createSection": True,
        "description": "informacje o autorze strony"
    }
    cms.add_page_section(section)
    # cms.remove_page_section('new_section')
    # cms.edit_page_section('about', section)

    # print('page sections:')
    # print('------------------')
    # cms.get_page_sections()
    # print('------------------')
    # print('------------------')
    #
    # print('python:')
    # print('------------------')
    # print(cms.get_python_projects())
    # print('------------------')
    # print('------------------')
    #
    # print('games:')
    # print('------------------')
    # print(cms.get_games_projects())
    # print('------------------')
    # print('------------------')
    #
    # print('html:')
    # print('------------------')
    # print(cms.get_html_fragments())
    # print('------------------')
    # print('------------------')

    return render_template("admin.html", sections=cms.get_section_names())


# @app.route("/data/slider_items")
# @crossdomain(origin='*')
# def slider_items():
#     page_data = load_cms_lists(cms_settings_file)
#     sections = page_data.get('sections')
#     items = list(filter(lambda x: x.get('show_on_slide'), sections))
#     return jsonify(items)
#
#

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
