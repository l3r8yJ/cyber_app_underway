import requests
import sqlite3
import lxml
import requests.api
from bs4 import BeautifulSoup, element


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
            
    def create_query_by_table(url, query_template):

        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        table = soup.find('tbody').find_all('tr')
        
        for row in table:
            element = '' 
            element += row.text.replace('\n', ',')
            element = element.split(',')
            element = list(filter(None, element))     
            
            for i in range(len(element)):
                element_query = ''

                if i == 0:
                    element_query += '(' + '\'' + element[i] + '\'' + ','

                elif i == len(element) - 1:
                    element_query += element[i] + '),\n'

                else:
                    element_query += element[i] + ','

                query_template += element_query

        query_template = query_template[: -2] + ';'
        
        return query_template
         