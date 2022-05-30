import json
import os
from time import sleep
import requests
import re
from PIL import Image
from io import BytesIO
from pyquery import PyQuery
from werkzeug.utils import secure_filename

wiki_adress = 'https://pl.wikipedia.org'
nba_final_mvps_addr = '/wiki/Bill_Russell_NBA_Finals_Most_Valuable_Player_Award'
img_dir = 'temp_imgs'


def write_data_to_file(file_path, data):
    with open(file_path, 'w') as file:
        data_as_json = json.dumps(data, indent=4)
        file.write(data_as_json)
        return True
    return False


def read_from_file(file_path):
    data = ''
    if not (os.path.isfile(file_path)):
        pass
    else:
        with open(file_path, 'r', encoding='utf8') as file:
            for line in file:
                data += line
        return data


def get_players():
    players = {}
    page = PyQuery(requests.get(wiki_adress + nba_final_mvps_addr).text)
    table = page('.wikitable.sortable:first')
    for row in table('tr').items():
        mvp_year = row('td:first').text()
        anchor = row('a:first')

        if mvp_year and anchor:
            player_name = anchor.text()
            player_id = '_'.join(player_name.split(' '))
            player_link = anchor.attr('href')
            if players.get(player_id):
                years = (players[player_id])['years']
                years.append(mvp_year)
            else:
                players[player_id] = {
                    'years': [mvp_year],
                    'name': player_name,
                    'link': wiki_adress + player_link
                }
    return players


def get_player_summary(elements_to_parse):
    i = 1
    summary = ''
    break_loop = False
    while not break_loop:
        elem = elements_to_parse[i]
        if elem.tag == 'p':
            paragraph = PyQuery(elem)
            summary += paragraph.text()
        elif elem.tag == 'div' and elem.get('class') == 'thumb tright':
            pass
        else:
            break_loop = True
        i = i + 1
    summary = re.sub('\\[\\d+\\]', '', summary)
    return summary


def get_player_img_and_summary(wiki_adress):
    page = PyQuery(requests.get(wiki_adress).text)
    player_img_link = page('.mw-parser-output .infobox a.image').attr('href')
    elements_to_parse = page('.mw-parser-output').children()
    player_summary = get_player_summary(elements_to_parse)
    return player_img_link, player_summary


def add_players_img_src_summary(players):
    for player in players.values():
        print('updating player: {}'.format(player['name']))
        [img_link, summary] = get_player_img_and_summary(player['link'])
        player['wikipedia_image'] = wiki_adress + img_link
        player['summary'] = summary
        sleep(10)


def get_and_save_image(dir, image_url):
    image_name = image_url.split('/')[-1]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
    }
    file_name = os.path.join(dir, secure_filename(image_name))
    if not (os.path.exists(file_name)):
        r = requests.get(image_url, stream=True, headers=headers)
        if r.ok:
            try:
                f = open(file_name, 'wb')
                for chunk in r.iter_content(chunk_size=128):
                    f.write(chunk)
                f.close()
                print('image saved: {}'.format(file_name))
            except Exception:
                print(Exception)


# Getting player names from wikipedia Final MVPs Page
#     players = get_players()
#     write_data_to_file('players.json', players)

# Adding summary and wikipedia image link

# players = json.loads(read_from_file('players.json'))
# add_players_img_src_summary(players)
# write_data_to_file('players.json', players)


# Downloading player images
# players = json.loads(read_from_file('players.json'))
#
# for player in players.values():
#     print('getting player {} image'.format(player['name']))
#     img_link = player['wikipedia_image']
#     image_page = PyQuery(requests.get(img_link).text)
#     image_url = 'https://' + image_page('.mw-body-content .fullImageLink a').attr('href')[2:]
#     player['image_name'] = secure_filename(image_url.split('/')[-1])
#     get_and_save_image(img_dir, image_url)
#     sleep(5)
#
# print('saving players data')
# write_data_to_file('players.json', players)


# Get player quotes from wikiquote

# players = json.loads(read_from_file('players.json'))
# for player in players.values():
#     quotes_array = []
#     print('getting player {} quotes'.format(player['name']))
#     name = '_'.join(player['name'].split(' '))
#     wiki_quote_link = 'https://pl.wikiquote.org/w/index.php?title={}&action=edit'.format(name)
#     page = PyQuery(requests.get(wiki_quote_link).text)
#     quote_source = page('#wpTextbox1.mw-editfont-monospace').text()
#     quotes_array = re.findall(r"(?:^\*\s)(.+)(?:\n)", quote_source, re.MULTILINE)
#     player['quotes'] = quotes_array
#     sleep(5)
#
# print('saving players data')
# write_data_to_file('players.json', players)


