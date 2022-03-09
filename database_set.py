import data_manager
import parser_hltv

manager = data_manager

teams_url = 'https://www.hltv.org/stats/teams'
ftu_url = 'https://www.hltv.org/stats/teams/ftu'
players_url = 'https://www.hltv.org/stats/players'

players_template = """
    INSERT INTO 
        players (full_name, maps, rounds, kd_diff, kd, rating)
    VALUES
"""

connection = manager.create_connection('testing_db')
query = parser_hltv.create_query_by_table(players_url, players_template)
manager.execute_query(connection, query)
print(query)
