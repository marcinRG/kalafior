import os


def check_file(directory, file):
    if directory and file:
        path_to_file = os.path.join(directory, file)
        return os.path.isfile(path_to_file)
    return False
