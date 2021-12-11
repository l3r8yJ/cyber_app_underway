import requests
import sqlite3
import lxml
import requests.api
from bs4 import BeautifulSoup


class ParserHLTV:
    url = 'https://www.hltv.org/stats/players'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")

    def create_html_from_req(self):
        f = open('site.html', 'w')
        f.write(self.req.text)

    def get_players_query(self):

        table = self.soup.find('tbody').find_all('tr')

        query = """
                INSERT INTO 
                    players (full_name, maps, rounds, kd_diff, kd, rating)
                VALUES              
            """

        for row in table:
            single_player = ''
            single_player += row.text.replace('\n', ',')
            single_player = single_player.split(',')
            single_player = list(filter(None, single_player))
            # print(single_player)

            for i in range(len(single_player)):
                player_query = ''

                if i == 0:
                    player_query += '(' + '\'' + single_player[i] + '\'' + ','

                elif i == len(single_player) - 1:
                    player_query += single_player[i] + '),\n'

                else:
                    player_query += single_player[i] + ','

                query += player_query

        query = query[: -2] + ';'
        return query
