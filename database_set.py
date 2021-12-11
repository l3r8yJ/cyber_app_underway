import data_manager
import parser_hltv

manager = data_manager

connection = manager.create_connection('testing_db')
query = parser_hltv.ParserHLTV.get_players_query(parser_hltv.ParserHLTV())
manager.execute_query(connection, query)
