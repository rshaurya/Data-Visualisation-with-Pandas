from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

symbol_dict = ['BTC', 'ETH', 'ADA', 'MATIC', 'DOGE', 'BUSD', 'SOL', 'LTC', 'ATOM', 'MIOTA',
               'LN', 'LUSD', 'HNT', 'LQTY', 'SYS', 'ANT', 'BCD', 'TROY', 'XPR', 'AUTO',
               'DMD', 'CRTS', 'OOE', 'QSP', 'BTSE', 'MAN', 'CRPT', 'BASIC', 'NAV',
               'STAKE', 'CRP', 'PROB', 'SHFT', 'KARMA', 'ATRI', 'SLIM', 'LITH', 'UNB',
               'ADS', 'BTS', 'EUROC', 'ETN']


class HomeScreen(Screen):
    pass

class OverviewScreen(Screen):
    pass


class MarketScreen(Screen):
    def on_enter(self, *args):
        from card import Example, MD3Card
        
    
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
