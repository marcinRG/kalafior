def import_text_to_list(file_name):
    list_txt = []
    try:
        txt_file = open(file_name, mode='r', encoding='UTF-8')
        for line in txt_file:
            list_txt.append(line[(line.find('>') + 1):line.rfind('<')])
    finally:
        return list_txt
