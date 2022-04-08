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

    def login(self, user_data):
        if user_data.get('login') and user_data.get('password'):
            admin = self.__get_admin()
            if admin.get('login') == user_data.get('login') and (user_data.get('password') == admin.get('password')):
                return {
                    'logged': True,
                    'user': admin.get('login')
                }
        return None

    def get_user_name(self):
        admin = self.__get_admin()
        return admin.get('login')

    def get_section_names(self):
        list_res = self.__get_settings()['resources']
        return [{'title': element['title'], 'id': element['id']} for element in list_res]

    def get_collections_names(self):
        list_res = self.__get_settings()['resources']
        return [{'title': element['title'], 'id': element['id'], 'description': element['description']} for element in
                list_res if element['fill_type'] == 'Collection']

    def get_fill_types(self):
        return self.__get_settings()['fill_types']

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
            self.__write_new_values_to_file(collection_id, collection)

    def __find_element(self, collection_id, id_element):
        collection = self.__get_data_collection(collection_id)
        index = find_index_in_dict_list('id', id_element, collection)
        if index >= 0:
            return collection[index]

    # Sections ---------------------------------------------

    def add_page_section(self, new_section):
        self.__add_new_element('sections', new_section)

    def edit_page_section(self, id_section, new_value):
        self.__edit_element('sections', id_section, new_value)

    def remove_page_section(self, id_section):
        self.__remove_element('sections', id_section)

    def get_page_sections(self):
        return self.__get_data_collection('sections')

    def get_page_section(self, id_section):
        return self.__find_element('sections', id_section)

    # Sections --------------------------------------------- end
    # Projects ---------------------------------------------
    def get_python_projects(self):
        return self.__get_data_collection('python')

    def add_project(self, new_project):
        self.__add_new_element('python', new_project)

    def edit_project(self, id_project, new_value):
        self.__edit_element('python', id_project, new_value)

    def remove_project(self, id_project):
        print('remove project')
        self.__remove_element('python', id_project)

    def get_python_project(self, id_project):
        return self.__find_element('python', id_project)

    # Projects -------------------------------------------end
    # Games -------------------------------------------------
    def get_games_projects(self):
        return self.__get_data_collection('games')

    def add_game(self, new_game):
        self.__add_new_element('games', new_game)

    def edit_game(self, id_game, new_value):
        self.__edit_element('games', id_game, new_value)

    def remove_game(self, id_game):
        self.__remove_element('games', id_game)

    def get_game_project(self, id_game):
        return self.__find_element('games', id_game)

    # Games -----------------------------------------------end
    # HTML Fragments -----------------------------------------------

    def get_html_fragments(self):
        return self.__get_data_collection('html_parts')

    def add_html_fragment(self, new_fragment):
        self.__add_new_element('html_parts', new_fragment)

    def edit_html_fragment(self, id_fragment, new_value):
        self.__edit_element('html_parts', id_fragment, new_value)

    def remove_html_fragment(self, id_fragment):
        self.__remove_element('html_parts', id_fragment)

    def get_html_fragment(self, id_fragment):
        return self.__find_element('html_parts', id_fragment)

    # HTML Fragments ----------------------------------------------- end

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
