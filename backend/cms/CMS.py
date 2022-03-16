import os

from utils.find_index_in_dict_list import find_index_in_dict_list
from utils.read_data_from_file import read_data_from_file
from utils.write_data_to_file import write_data_to_file


class CMS:
    __settings_name = 'settings'
    __admin_name = 'admin'

    def __init__(self, main_dir, admin_file, cms_settings_file):
        if os.path.exists(main_dir):
            self.main_dir = main_dir
            self.__initialize_data_from_file(self.__admin_name, self.main_dir, admin_file)
            self.__initialize_data_from_file(self.__settings_name, self.main_dir, cms_settings_file)
        os.listdir(self.main_dir)

    def print_settings(self):
        list_res = self.__get_settings()['resources']
        print(list_res)

    def get_section_names(self):
        list_res = self.__get_settings()['resources']
        return [{'title': element['title'], 'id': element['id']} for element in list_res]

    def __write_new_values_to_file(self, resource_id, data):
        settings = [element for element in self.__get_settings()['resources'] if element['id'] == resource_id][0]
        file = self.__get_resource_file(settings)
        write_data_to_file(file, data)

    def __add_new_element(self, collection_id, new_element):
        collection = self.__get_data_collection(collection_id)
        collection.append(new_element)
        self.__write_new_values_to_file(collection_id, collection)

    def __edit_element(self, collection_id, id_element, new_value):
        collection = self.__get_data_collection(collection_id)
        index = find_index_in_dict_list('id', id_element, collection)
        if index >= 0:
            collection[index] = new_value
            self.__write_new_values_to_file(collection_id, collection)

    def __remove_element(self, collection_id, id_element):
        collection = self.__get_data_collection(collection_id)
        index = find_index_in_dict_list('id', id_element, collection)
        if index >= 0:
            collection.pop(index)
            self.__write_new_values_to_file('sections', collection)

    def add_page_section(self, new_section):
        self.__add_new_element('sections', new_section)

    def edit_page_section(self, id_section, new_value):
        self.__edit_element('sections', id_section, new_value)

    def remove_page_section(self, id_section):
        self.__remove_element('sections', id_section)

    def get_page_sections(self):
        return self.__get_data_collection('sections')

    def get_python_projects(self):
        return self.__get_data_collection('python')

    def get_games_projects(self):
        return self.__get_data_collection('games')

    def get_html_fragments(self):
        return self.__get_data_collection('html_parts')

    def __get_resource_file(self, settings):
        path_to_resources = self.__get_settings()['path_data']
        return os.path.join(os.path.join(self.main_dir, path_to_resources), settings['resource_name'])

    def __get_data_collection(self, id_collection):
        data = None
        settings = list(filter(lambda v: v['id'] == id_collection, self.__get_settings()['resources']))[0]
        file = self.__get_resource_file(settings)

        if settings['type'] == 'file':
            data = read_data_from_file(file)
        elif settings['type'] == 'directory':
            data = os.listdir(file)
        return data

    def __get_admin(self):
        return getattr(self, self.__admin_name)

    def __get_settings(self):
        return getattr(self, self.__settings_name)

    def __initialize_data_from_file(self, property_name, directory, path_to_file):
        path = os.path.join(directory, path_to_file)
        if os.path.exists(path):
            data = read_data_from_file(path)
            setattr(self, property_name, data)

# def get_games_app(self):
#     print('get games app')
#
# def get_pythons_app(self):
#     print('get games app')
#
# def get_page_sections(self):
#     print('get page sections')
#
# def get_html_fragments(self):
#     print('get html fragments')
#
# def add_html_fragment(self):
#     pass
#
# def add_page_section(self):
#     pass
#
# def remove_page_section(self):
#     pass
#
# def change_page_section(self):
#     pass
