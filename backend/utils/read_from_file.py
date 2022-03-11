import os


def read_from_file(file_path):
    data = ''
    if not (os.path.isfile(file_path)):
        pass
    else:
        with open(file_path, 'r', encoding='utf8') as file:
            for line in file:
                data += line
        return data
