from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.stacklayout import StackLayout

import pandas as pd
import matplotlib.pyplot as plt
from kivy.core.window import Window



class HomeScreen(Screen):
    def __init__(self, **kw):
        return super(HomeScreen, self).__init__(**kw)
    
    def on_enter(self, *args):
        Window.maximize()
        return super(HomeScreen, self).on_enter(*args)
    

class OverviewScreen(Screen):
    pass


class MarketScreen(Screen):
    def on_enter(self, *args):
        from card import Market, MD3Card
            
class HistoryScreen(Screen):
    pass
        

class MainApp(MDApp):
    def build(self):
        Builder.load_file("main2.kv")

        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home_screen"))
        sm.add_widget(OverviewScreen(name="overview_screen"))
        sm.add_widget(MarketScreen(name="market_screen"))
        sm.add_widget(HistoryScreen(name="history_screen"))

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_hue = "200"
        return sm

MainApp().run()
