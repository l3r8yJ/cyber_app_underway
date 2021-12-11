from kivy.app import App
from kivy.lang import Builder
from windows import InfoWindow, NewsWindow, MainWindow, WindowManager
import StackLayoutPlayers

load = Builder.load_file('main.kv')


class MainApp(App):
    def build(self):
        return load
    

if __name__ == '__main__':
    MainApp().run()
