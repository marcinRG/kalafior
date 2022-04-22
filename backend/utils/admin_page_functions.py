import os

from werkzeug.utils import secure_filename

from utils.is_not_empty import is_not_empty
from utils.request_functions import remove_from_dict, split_tags, change_string_2_bool, allowed_file


def edit_or_add_new(request_args, page, edit_function, new_function):
    copy = clean_post_request(request_args, page)
    if request_args.get('edit_mode') == 'edit':
        edit_function(copy.get('id'), copy)
    elif request_args.get('edit_mode') == 'new':
        new_function(copy)


def clean_post_request(request_args, page):
    request_copy = dict(request_args)
    request_copy = remove_from_dict(request_copy, 'form_type')
    request_copy = remove_from_dict(request_copy, 'edit_mode')
    if page == 'sections':
        request_copy = clean_fill_page_options(request_copy)
    if page == 'python':
        tags = split_tags(request_copy['tags'])
        request_copy['tags'] = tags
    request_copy = change_string_2_bool(request_copy)
    return request_copy


def clean_fill_page_options(request_args):
    copy = dict(request_args)
    fill_options = copy.get('fill_options')
    if fill_options is not None:
        if fill_options == 'HTML_part':
            copy = remove_from_dict(copy, 'collection_options')
        elif fill_options == 'Collection':
            copy = remove_from_dict(copy, 'html_options')
        elif fill_options == 'None':
            copy = remove_from_dict(copy, 'html_options')
            copy = remove_from_dict(copy, 'collection_options')
    else:
        copy['fill_options'] = 'None'
    return copy


def get_page_address(page):
    pages_address = {
        'sections': '/admin/sections.html',
        'python': '/admin/python.html',
        'games': '/admin/games.html',
        'html_parts': 'admin/html_parts.html'
    }
    # page_adr = '/admin/sections.html'
    # selected_page = pages_address.get(page)
    # if selected_page:
    #     page_adr = selected_page
    # return page_adr

    return pages_address.get(page)


def get_list_content(page, cms):
    page_content = None
    if page == 'sections':
        page_content = cms.get_page_sections()
    elif page == 'python':
        page_content = cms.get_python_projects()
    elif page == 'games':
        page_content = cms.get_games_projects()
    elif page == 'html_parts':
        page_content = cms.get_html_fragments()
    return page_content


def get_content_edit_element(page, id_element, cms):
    if page == 'sections':
        data = cms.get_page_section(id_element)
    elif page == 'python':
        data = cms.get_python_project(id_element)
    elif page == 'games':
        data = cms.get_game_project(id_element)
    elif page == 'html_parts':
        data = cms.get_html_fragment(id_element)
    return data


def handle_post_request(request_args, request_files, page, cms, file_extensions, path):
    if page == 'sections' and request_args.get('form_type') == 'sections_form':
        edit_or_add_new(request_args, page, cms.edit_page_section, cms.add_page_section)

    if page == 'python' and request_args.get('form_type') == 'python_form':
        file_name = save_file(request_files, file_extensions, path)
        if file_name:
            request_args['image'] = file_name
        edit_or_add_new(request_args, page, cms.edit_project, cms.add_project)

    if page == 'html_parts' and request_args.get('form_type') == 'html_parts_form':
        print('you are here pages')
        edit_or_add_new(request_args, page, cms.edit_html_fragment, cms.add_html_fragment)

    if page == 'games' and request_args.get('form_type') == 'games_form':
        edit_or_add_new(request_args, page, cms.edit_game, cms.add_game)


def save_file(request_files, file_extensions, path):
    if 'file' in request_files:
        file = request_files['file']
        if file and allowed_file(file.filename, file_extensions):
            filename = secure_filename(file.filename)
            file.save(os.path.join(path, filename))
            return filename


def remove_element(id_elem, page, cms):
    if page == 'sections':
        cms.remove_page_section(id_elem)
    elif page == 'python':
        cms.remove_project(id_elem)
    elif page == 'games':
        cms.remove_game(id_elem)
    elif page == 'html_parts':
        cms.remove_html_fragment(id_elem)
