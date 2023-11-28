from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.button import MDIconButton

from kivymd.app import MDApp
from kivymd.uix.card import MDCard

image_list = ['symbol_images/btc.png', 'symbol_images/eth.png', 'symbol_images/ada.png', 
     'symbol_images/matic.png', 'symbol_images/doge.png', 'symbol_images/busd.png',
     'symbol_images/sol.png', 'symbol_images/ltc.png', 'symbol_images/atom.png',
     'symbol_images/miota.png', 'symbol_images/link.png', 'symbol_images/btg.png',
     'symbol_images/hnt.png', 'symbol_images/lqty.png', 'symbol_images/sys.png',
     'symbol_images/ant.png', 'symbol_images/bcd.png', 'symbol_images/trx.png',
     'symbol_images/xpr.png', 'symbol_images/avax.png', 'symbol_images/dmd.png',
     'symbol_images/imx10603.png', 'symbol_images/ocean.png', 'symbol_images/qsp.png',
     'symbol_images/neo.png', 'symbol_images/mana.png', 'symbol_images/crpt.png',
     'symbol_images/bat.png', 'symbol_images/nav.png', 'symbol_images/stake.png',
     'symbol_images/comp5692.png', 'symbol_images/nexo.png', 'symbol_images/celo.png',
     'symbol_images/karma.png', 'symbol_images/agix.png', 'symbol_images/qkc.png',
     'symbol_images/cennz.png', 'symbol_images/rune.png', 'symbol_images/dot.png',
     'symbol_images/bts.png', 'symbol_images/eurs.png', 'symbol_images/etn.png']

symbol_list = ['BTC', 'ETH', 'ADA', 'MATIC', 'DOGE', 'BUSD', 'SOL', 'LTC', 'ATOM', 'MIOTA',
               'LINK', 'BTG', 'HNT', 'LQTY', 'SYS', 'ANT', 'BCD', 'TRX', 'XPR', 'AVAX',
               'DMD', 'IMX10603', 'OCEAN', 'QSP', 'NEO', 'MANA', 'CRPT', 'BAT', 'NAV',
               'STAKE', 'COMP5692', 'NEXO', 'CELO', 'KARMA', 'AGIX', 'QKC', 'CENNZ', 'RUNE',
               'DOT', 'BTS', 'EURS', 'ETN']


class MD3Card(MDCard):
    '''Implements a material design v3 card.'''

    text = StringProperty()
    icon = StringProperty()

    def __init__(self, **kwargs):
        super(MD3Card, self).__init__(**kwargs)
        self.icon = kwargs.get('icon', '')
    
    def on_icon(self, instance, value):
        # Do something with the icon, e.g., update the card's UI based on the new icon
        print(f"Icon changed to: {value}")

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('card.kv')

    def on_start(self):
        for i in symbol_list:
            self.root.ids.stack.add_widget(
                MD3Card(
                    line_color=(0.2, 0.2, 0.2, 0.8),
                    style="elevated",
                    text=i,
                    md_bg_color="##171717",
                    shadow_offset=(0, -1),
                    icon=image_list[symbol_list.index(i)]
                )
            )




Example().run()