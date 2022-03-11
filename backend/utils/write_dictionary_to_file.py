import json


def write_data_to_file(file_path, data):
    if isinstance(data, dict):
        with open(file_path, 'w', encoding='utf8') as file:
            data_as_json = json.dumps(data, encoding='utf8')
            file.write(data_as_json)
            return True
    return False
