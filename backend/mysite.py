import os
from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename

from blueprints.main_routes import main_routes
from blueprints.pass_generator import password_generator
from blueprints.winnie_the_pooh import kubus
from cms.CMS import CMS
from cms.cms_settings_file import cms_settings_file, cms_images_folder
from cms.cms_settings_file import cms_admin
from utils.request_functions import edit_or_add_new, allowed_file

app = Flask(__name__)
app.secret_key = 'NFcT&jCOn#ekRB~qyh9gSAso*l2+pXYUwDHt!PI5'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'svg']
app.config['APP_IMAGES'] = '/admin/assets/images/'
app.config['UPLOAD_FOLDER'] = cms_images_folder

app.register_blueprint(kubus)
app.register_blueprint(password_generator)
app.register_blueprint(main_routes)

cms = CMS(os.getcwd(), cms_admin, cms_settings_file)


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
            return redirect('/admin/' + page)
        return handle_get_request(get_request, page)
    else:
        return redirect('/login')


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


@app.route("/", methods=['POST', 'GET', 'OPTIONS'])
def main():
    menu_items = [element for element in cms.get_page_sections() if element.get('show_on_menu') is not None]
    sections = cms.get_page_sections()
    return render_template('main/index.html', menu_items=menu_items, sections=sections)


if __name__ == '__main__':
    app.run(debug=True)
