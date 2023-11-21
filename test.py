from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.card import MDCard

KV = '''
<MD3Card>
    padding: 4
    size_hint: None, None
    size: "200dp", "100dp"

    MDRelativeLayout:
		id: relative

        MDIconButton:
            icon: "symbol_images/btc.png"
            icon_size: "80dp"
            pos_hint: {"top": 1, "right": 1}
            on_press: 
        

        MDLabel:
            id: label
            text: root.text
            adaptive_size: True
            color: "grey"
            pos: "12dp", "12dp"
            bold: True


MDScreen:

    StackLayout:
        id: box
        spacing: [50, 30]
        padding: [50, 200, 0, 0]
        adaptive_size: True
'''


class MD3Card(MDCard):
    '''Implements a material design v3 card.'''

    text = StringProperty()

symbol_dict = ['BTC', 'ETH', 'ADA', 'MATIC', 'DOGE', 'BUSD', 'SOL', 'LTC', 'ATOM', 'MIOTA',
               'LN', 'LUSD', 'HNT', 'LQTY', 'SYS', 'ANT', 'BCD', 'TROY', 'XPR', 'AUTO',
               'DMD', 'CRTS', 'OOE', 'QSP', 'BTSE', 'MAN', 'CRPT', 'BASIC', 'NAV',
               'STAKE', 'CRP', 'PROB', 'SHFT', 'KARMA', 'ATRI', 'SLIM', 'LITH', 'UNB',
               'ADS', 'BTS', 'EUROC', 'ETN']

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

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