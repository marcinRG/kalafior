import json

from utils.read_from_file import read_from_file


def read_data_from_file(file_path):
    data_txt = read_from_file(file_path)
    if data_txt:
        return json.loads(data_txt)
