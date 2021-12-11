import requests
import sqlite3
import lxml
import requests.api
from bs4 import BeautifulSoup


class ParserHLTV:
    
    players_url = 'https://www.hltv.org/stats/players'
    players_req = requests.get(players_url)
    players_soup = BeautifulSoup(players_req.text, "lxml")
    
    teams_url = 'https://www.hltv.org/stats/teams'
    teams_req = requests.get(teams_url)
    teams_soup = BeautifulSoup(teams_req.text, "lxml")
    
    ftu_url = 'https://www.hltv.org/stats/teams/ftu'
    ftu_req = requests.get(ftu_url)
    ftu_soup = BeautifulSoup(ftu_req.text, 'lxml')
    

    def get_players_query(self):

        players_table = self.players_soup.find('tbody').find_all('tr')

        final_player_query = """
                INSERT INTO 
                    players (full_name, maps, rounds, kd_diff, kd, rating)
                VALUES              
            """

        for row in players_table:
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

                final_player_query += player_query

        final_player_query = final_player_query[: -2] + ';'
        return final_player_query

    def get_teams_query(self):
        teams_table = self.teams_soup.find('tbody').find_all('tr')
        
        for row in teams_table:
            single_team = ''
            single_team += row.text.replace('\n', ',')
            single_team = single_team.split(',')
            single_team = list(filter(None, single_team))
            
            print(single_team)     
            
    def get_ftu_query(self):
        ftu_table = self.ftu_soup.find('tbody').find_all('tr')
        
        for row in ftu_table:
            single_ftu = ''
            single_ftu += row.text.replace('\n', ',')
            single_ftu = single_ftu.split(',')
            single_ftu = list(filter(None, single_ftu))
            print(single_ftu)
         