import json
import os
import requests
from pyquery import PyQuery

wiki_adress = 'https://pl.wikipedia.org'
nba_final_mvps_addr = '/wiki/Bill_Russell_NBA_Finals_Most_Valuable_Player_Award'


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



players = json.loads(read_from_file('players.json'))
print((players['Michael_Jordan'])['link'])

#page = PyQuery(requests.get('https://pl.wikipedia.org/wiki/Michael_Jordan').text)
# paragraphs = page('.mw-parser-output').children('p')


# player = players['Michael_Jordan']
# write_data_to_file('players.json',players)
