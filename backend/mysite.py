import os
from flask import Flask, render_template, request, send_from_directory, jsonify, redirect, url_for, g, session
from werkzeug.utils import secure_filename

from cms.CMS import CMS
from utils.crossdomain import crossdomain
from utils.generate_password import generate_password
from utils.import_text_to_list import import_text_to_list
from cms.cms_settings_file import cms_settings_file, cms_images_folder
from cms.cms_settings_file import cms_admin
from utils.request_functions import edit_or_add_new, allowed_file

app = Flask(__name__)
app.secret_key = 'NFcT&jCOn#ekRB~qyh9gSAso*l2+pXYUwDHt!PI5'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'svg']
app.config['UPLOAD_FOLDER'] = cms_images_folder
cms = CMS(os.getcwd(), cms_admin, cms_settings_file)

pages_address = {
    'sections': '/admin/sections.html',
    'python': '/admin/python.html',
    'games': '/admin/games.html',
    'html_parts': 'admin/html_parts.html'
}


def login_user(user_data):
    is_logged_in = cms.login(user_data)
    if is_logged_in.get('logged') is True:
        session['login'] = is_logged_in.get('user')
        session['logged_in'] = is_logged_in.get('logged')


def is_user_logged_in():
    return session.get('logged_in') is True and session.get('login') == cms.get_user_name()


def get_session_data():
    if is_user_logged_in():
        return {
            'login': session.get('login'),
            'logged_in': session.get('logged_in')
        }
    return None


def log_out():
    session.pop('login')
    session.pop('logged_in')


def get_page_address(page):
    page_adr = '/admin/sections.html'
    selected_page = pages_address.get(page)
    if selected_page:
        page_adr = selected_page
    return page_adr


def get_list_content(page):
    page_content = []
    if page == 'sections':
        page_content = cms.get_page_sections()
    if page == 'python':
        page_content = cms.get_python_projects()
    if page == 'games':
        page_content = cms.get_games_projects()
    if page == 'html_parts':
        page_content = cms.get_html_fragments()
    return page_content


def get_content_edit_element(page, id_element):
    data = {}
    if page == 'sections':
        data = cms.get_page_section(id_element)
    if page == 'python':
        data = cms.get_python_project(id_element)
    if page == 'games':
        data = cms.get_game_project(id_element)
    if page == 'html_parts':
        data = cms.get_html_fragment(id_element)
    return data


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'images/favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/login', methods=['GET', 'POST', 'OPTIONS'])
def login():
    post_data = request.form.to_dict()
    if post_data.get('form_type') == 'login_form':
        login_user(post_data)
        if is_user_logged_in():
            return redirect('admin/sections')
        else:
            return redirect('login')
    return render_template("admin/login.html")


def handle_post_request(request_args, page):
    if page == 'sections' and request_args.get('form_type') == 'sections_form':
        edit_or_add_new(request_args, cms.edit_page_section, cms.add_page_section)
    return redirect('/admin/' + page)


def handle_get_request(request_args, page):
    mode = 'list'
    data = []
    if request_args.get('logout') == 'ok':
        log_out()
        return redirect('/login')

    if request_args.get('mode'):
        mode = request_args.get('mode')

    if mode == 'list':
        data = get_list_content(page)

    if mode == 'edit':
        id_elem = request_args.get('id_elem')
        data = get_content_edit_element(page, id_elem)
        print(data)

    if mode == 'remove':
        if request_args.get('id_elem'):
            cms.remove_page_section(request_args.get('id_elem'))
        return redirect('/admin/' + page)

    if mode == 'new':
        data = {}

    return render_template(get_page_address(page), page_content=data,
                           sections=cms.get_section_names(), fill_types=cms.get_fill_types(),
                           collection_names=cms.get_collections_names(), html_parts_names=cms.get_html_fragments(),
                           page=page, user_data=get_session_data(), mode=mode)


@app.route("/admin/<page>", methods=['GET', 'POST', 'OPTIONS'])
def admin(page):
    print('here we go')
    if is_user_logged_in():
        if request.method == 'POST':
            post_request = request.form.to_dict()
            handle_post_request(post_request, page)

        if request.method == 'GET':
            get_request = request.args.to_dict()

        return handle_get_request(get_request, page)
    else:
        return redirect('/login')


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


@app.route("/test", methods=['POST', 'GET', 'OPTIONS'])
def test_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename, ALLOWED_EXTENSIONS):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(request.url)
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
