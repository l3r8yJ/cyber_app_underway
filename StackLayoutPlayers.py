from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from kivy.metrics import dp
import parser_hltv
import data_manager as dm

connection = dm.create_connection('testing_db')


class PlayerButton(Button, ScreenManager):
    def on_press(self):
        print(self.name + ' was pressed')
        get_player_query = 'SELECT * FROM players WHERE full_name = ' + '\'' + self.name + '\''
        player = dm.execute_read_query(connection, get_player_query)

        for data in player:
            for fields in data:
                print(fields)


class StackLayoutPlayers(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        players = dm.execute_read_query(connection, 'SELECT full_name FROM players WHERE id < 50')

        # Create buttons for each player
        for player in players:
            for nick in player:
                size = dp(80)
                button = PlayerButton(text=str(nick), size_hint=(None, None), size=(size, size))
                button.name = str(nick)
                self.add_widget(button)
