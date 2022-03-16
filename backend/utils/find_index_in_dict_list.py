def find_index_in_dict_list(key, value, dict_list):
    found_index = [i for i, element in enumerate(dict_list) if element[key] == value]
    if len(found_index) == 1:
        return found_index[0]
    return -1
