from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.card import MDCard


symbol_dict = ['BTC', 'ETH', 'ADA', 'MATIC', 'DOGE', 'BUSD', 'SOL', 'LTC', 'ATOM', 'MIOTA',
               'LN', 'LUSD', 'HNT', 'LQTY', 'SYS', 'ANT', 'BCD', 'TROY', 'XPR', 'AUTO',
               'DMD', 'CRTS', 'OOE', 'QSP', 'BTSE', 'MAN', 'CRPT', 'BASIC', 'NAV',
               'STAKE', 'CRP', 'PROB', 'SHFT', 'KARMA', 'ATRI', 'SLIM', 'LITH', 'UNB',
               'ADS', 'BTS', 'EUROC', 'ETN']


class MD3Card(MDCard):
    '''Implements a material design v3 card.'''

    text = StringProperty()


class Example(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_file('card.kv')

    def on_start(self):
        for i in symbol_dict:
            self.root.ids.box.add_widget(
                MD3Card(
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    style="elevated",
                    text=i,
                    md_bg_color="##171717",
                    shadow_offset=(0, -1),
                )
            )


Example().run()