import os

from utils.read_data_from_file import read_data_from_file


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
        return list(map(lambda x: {'title': x['title'], 'id': x['id']}, list_res))

    def get_page_sections(self):
        return self.__get_data_collection('sections')

    def get_python_projects(self):
        return self.__get_data_collection('python')

    def get_games_projects(self):
        return self.__get_data_collection('games')

    def get_html_fragments(self):
        return self.__get_data_collection('html_parts')

    def __get_data_collection(self, id_collection):
        data = None
        path_to_resources = self.__get_settings()['path_data']
        settings = list(filter(lambda v: v['id'] == id_collection, self.__get_settings()['resources']))[0]
        file = os.path.join(os.path.join(self.main_dir, path_to_resources), settings['resource_name'])

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
