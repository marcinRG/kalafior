from utils.is_not_empty import is_not_empty
from utils.read_data_from_file import read_data_from_file


def login_admin(post_data, admin_settings):
    logged = False
    admin_data = read_data_from_file(admin_settings)
    if (is_not_empty(admin_data) and is_not_empty(post_data)):
        start = True
        for key in admin_data.keys():
            if start:
                logged = (post_data[key] == admin_data[key])
                start = False
            else:
                logged = logged and (post_data[key] == admin_data[key])
    return logged
