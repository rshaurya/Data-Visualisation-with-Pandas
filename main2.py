from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

symbol_dict = ['BTC', 'ETH', 'ADA', 'MATIC', 'DOGE', 'BUSD', 'SOL', 'LTC', 'ATOM', 'MIOTA',
               'LN', 'LUSD', 'HNT', 'LQTY', 'SYS', 'ANT', 'BCD', 'TROY', 'XPR', 'AUTO',
               'DMD', 'CRTS', 'OOE', 'QSP', 'BTSE', 'MAN', 'CRPT', 'BASIC', 'NAV',
               'STAKE', 'CRP', 'PROB', 'SHFT', 'KARMA', 'ATRI', 'SLIM', 'LITH', 'UNB',
               'ADS', 'BTS', 'EUROC', 'ETN']


# Function to create dataframe from csv files 
# by taking 2 inputs: symbol and name of cryptocurrency


class HomeScreen(Screen):
    pass

class OverviewScreen(Screen):
    pass

class MD3Card(MDCard):
    text = StringProperty()

class MarketScreen(Screen, MDCard):

    # text = StringProperty()
    
    def Card(self):
        for i in symbol_dict:
            self.add_widget(
                MD3Card(
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    style="elevated",
                    text=i,
                    md_bg_color="##171717",
                    shadow_offset=(0, -1),
                )
            )
    
class MainApp(MDApp):
    def build(self):
        Builder.load_file("main2.kv")

        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home_screen"))
        sm.add_widget(OverviewScreen(name="overview_screen"))
        sm.add_widget(MarketScreen(name="market_screen"))

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_hue = "200"
        return sm
    
    
    


MainApp().run()
