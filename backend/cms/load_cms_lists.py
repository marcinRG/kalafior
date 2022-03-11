import os

from utils.is_not_empty import is_not_empty
from utils.read_data_from_file import read_data_from_file


def load_cms_lists(settings_file):
    settings = read_data_from_file(settings_file)
    if is_not_empty(settings):
        data_files = settings.get('data_files')
        path_to_resources = settings.get('path_data')
        return load_lists(path_to_resources, data_files)


def load_lists(path_to_resources, data_files):
    dict_data = {}
    for k, v in data_files.items():
        path_to_data_file = os.path.join(path_to_resources, v)
        data = read_data_from_file(path_to_data_file)
        if is_not_empty(data):
            dict_data[k] = data
    return dict_data
