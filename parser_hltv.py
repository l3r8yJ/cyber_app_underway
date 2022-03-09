import requests
import sqlite3
import lxml
import requests.api
from bs4 import BeautifulSoup


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

    query_template = query_template[:-2] + ';'

    return query_template
