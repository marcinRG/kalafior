def remove_from_dict(dictionary, key):
    copy = dict(dictionary)
    if copy.get(key) is not None:
        copy.pop(key)
    return copy


def change_string_2_bool(dictionary):
    copy = dict(dictionary)
    for key, value in copy.items():
        if value == 'True':
            copy[key] = True
    return copy


def edit_or_add_new(request_args, page, edit_function, new_function):
    copy = clean_post_request(request_args, page)
    print(copy)
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


def split_tags(tags_as_string):
    return [element.strip() for element in tags_as_string.split(',')]


def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
