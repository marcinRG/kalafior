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
app.config['APP_IMAGES'] = '/admin/assets/images/'
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
    elif page == 'python':
        page_content = cms.get_python_projects()
    elif page == 'games':
        page_content = cms.get_games_projects()
    elif page == 'html_parts':
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


def handle_post_request(request_args, request_files, page):
    if page == 'sections' and request_args.get('form_type') == 'sections_form':
        edit_or_add_new(request_args, page, cms.edit_page_section, cms.add_page_section)

    if page == 'python' and request_args.get('form_type') == 'python_form':
        file_name = save_file(request_files, ALLOWED_EXTENSIONS)
        if file_name:
            request_args['image'] = file_name
        edit_or_add_new(request_args, page, cms.edit_project, cms.add_project)

    if page == 'html_parts' and request_args.get('form_type') == 'html_parts_form':
        print('you are here pages')
        edit_or_add_new(request_args, page, cms.edit_html_fragment, cms.add_html_fragment)

    if page == 'games' and request_args.get('form_type') == 'games_form':
        edit_or_add_new(request_args, page, cms.edit_game, cms.add_game)

    return redirect('/admin/' + page)


def save_file(request_files, file_extensions):
    if 'file' in request_files:
        file = request.files['file']
        if file and allowed_file(file.filename, file_extensions):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return filename


def remove_element(id_elem, page):
    if page == 'sections':
        cms.remove_page_section(id_elem)
    elif page == 'python':
        cms.remove_project(id_elem)
    elif page == 'games':
        cms.remove_game(id_elem)
    elif page == 'html_parts':
        cms.remove_html_fragment(id_elem)


def handle_get_request(request_args, page):
    id_elem = request_args.get('id_elem')
    mode = request_args.get('mode')
    data = []

    if request_args.get('logout') == 'ok':
        log_out()
        return redirect('/login')

    if mode:
        if mode == 'edit' and id_elem:
            data = get_content_edit_element(page, id_elem)
        if mode == 'remove':
            if id_elem:
                remove_element(id_elem, page)
                return redirect('/admin/' + page)
        if mode == 'new':
            data = {}
    else:
        mode = 'list'
        data = get_list_content(page)

    print('nazwy kolekcji')
    print(cms.get_collections_names())
    print(cms.get_fill_types())

    return render_template(get_page_address(page), page_content=data,
                           sections=cms.get_section_names(), fill_types=cms.get_fill_types(),
                           collection_names=cms.get_collections_names(), html_parts_names=cms.get_html_fragments(),
                           page=page, user_data=get_session_data(), mode=mode)


@app.route("/admin/<page>", methods=['GET', 'POST', 'OPTIONS'])
def admin(page):
    if is_user_logged_in():
        get_request = request.args.to_dict()
        post_request = request.form.to_dict()
        request_files = request.files
        if request.method == 'POST':
            handle_post_request(post_request, request_files, page)
        return handle_get_request(get_request, page)
    else:
        return redirect('/login')


@app.route("/kubus_puchatek")
def puchatek():
    return render_template('puchatek/puchalke.html')


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
    return render_template('pass_genrator/pass_generator.html')


@app.route("/", methods=['POST', 'GET', 'OPTIONS'])
def main():
    menu_items = [element for element in cms.get_page_sections() if element.get('show_on_menu') is not None]
    sections = cms.get_page_sections()
    return render_template('main/index.html', menu_items=menu_items, sections=sections)


if __name__ == '__main__':
    app.run(debug=True)
