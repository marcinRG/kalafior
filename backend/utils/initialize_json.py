import os

from utils.write_dictionary_to_file import write_data_to_file


def initialize_json(path_to_file):
    if not (os.path.isfile(path_to_file)):
        file_content = {}
        write_data_to_file(path_to_file, file_content)
    return False
