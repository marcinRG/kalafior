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


def split_tags(tags_as_string):
    return [element.strip() for element in tags_as_string.split(',')]


def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
