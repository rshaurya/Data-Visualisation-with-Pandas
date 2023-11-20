from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import matplotlib.pyplot as plt
import pandas as pd



'''

Function to create dataframe from csv files 
by taking 2 inputs: symbol and name of cryptocurrency

'''

def crypto_dataframe(symbol, name):
    df = pd.read_csv('crypto-dataset/Price-Data/' + symbol + '_' + name + '.csv', index_col=0)
    return df


class HomeScreen(Screen):
    pass

class OverviewScreen(Screen):
    pass

class MarketScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        Builder.load_file("main2.kv")

        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home_screen"))
        sm.add_widget(OverviewScreen(name="next_screen"))
        sm.add_widget(MarketScreen(name="market_screen"))


        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_hue = "200"
        return sm


MainApp().run()
