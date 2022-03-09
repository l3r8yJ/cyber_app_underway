from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.metrics import dp
import data_manager as dm

connection = dm.create_connection('testing_db')
player_data = []


class PlayerButton(Button, ScreenManager):

    def on_press(self):
        print(self.name + ' was pressed')
        get_player_query = 'SELECT * FROM players WHERE full_name = ' + '\'' + self.name + '\''
        player_data = player = dm.execute_read_query(connection,
                                                     get_player_query)

        print(player_data)
        self.parent.parent.parent.parent.current = 'player_screen'


class StackLayoutPlayers(StackLayout):

    def __init__(self, **kwargs):
        super(StackLayoutPlayers, self).__init__(**kwargs)
        self.height = self.minimum_height
        players = dm.execute_read_query(
            connection, 'SELECT full_name FROM players WHERE id < 50')

        # Create buttons for each player
        for player in players:
            for nick in player:
                size = dp(80)

                button = PlayerButton(size_hint=(None, None),
                                      size=(size, size))
                button.id = str(nick)
                button.text = str(button.id)
                button.name = str(button.id)

                self.add_widget(button)


class Scroll(ScrollView):
    pass


class StackScreen(Screen):
    pass


class PlayerScreen(Screen):

    def on_realise(self, **kw):
        super(PlayerScreen, self).__init__(**kw)
        player_text = ''

        for data in player_data:
            player_text += str(data) + ' '

        label = Label(text=player_text)
        self.add_widget(label)


class InfoManger(ScreenManager):
    pass

    # def __init__(self, **kwargs):
    #     super(InfoManger, self).__init__(**kwargs)
    #     self.add_widget(PlayerScreen)
