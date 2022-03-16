import json


def write_data_to_file(file_path, data):
    with open(file_path, 'w') as file:
        data_as_json = json.dumps(data, indent=4)
        file.write(data_as_json)
        return True
    return False
