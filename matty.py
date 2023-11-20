from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivymd.uix.screen import MDScreen
import pandas as pd

symbol_dict = ['BTC', 'ETH', 'ADA', 'MATIC', 'DOGE', 'BUSD', 'SOL', 'LTC', 'ATOM', 'MIOTA',
               'LN', 'LUSD', 'HNT', 'LQTY', 'SYS', 'ANT', 'BCD', 'TROY', 'XPR', 'AUTO',
               'DMD', 'CRTS', 'OOE', 'QSP', 'BTSE', 'MAN', 'CRPT', 'BASIC', 'NAV',
               'STAKE', 'CRP', 'PROB', 'SHFT', 'KARMA', 'ATRI', 'SLIM', 'LITH', 'UNB',
               'ADS', 'BTS', 'EUROC', 'ETN']

class MD3Card(MDCard):
    '''Implements a material design v3 card.'''
    pass


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return (
            MDScreen(
                StackLayout(
                    id="stack",
                    orientation='lr-tb',
                    spacing=(50, 30),
                    padding=(50, 200, 0, 0)
                )
            )
        )

    def on_start(self):
        for i in symbol_dict:
                
            self.root.ids.stack.add_widget(
                MD3Card(

                    MDRelativeLayout(
                        MDIconButton(
                            icon="symbol_images/btc.png",
                            icon_size="50dp",
                            pos_hint={"top": 1, "right": 1}
                        ),
                        MDLabel(
                            text=str(i),
                            color="#0ee0e8",
                            pos=("12dp", "12dp")
                        ),
                    ),

                    line_color=(0.2, 0.2, 0.2, 0.8),
                    style="elevated",
                    padding="4dp",
                    size_hint=(None, None),
				    size=("250dp", "100dp"),
                    md_bg_color="##171717",
                    shadow_softness=2,
                    shadow_offset=(0, 1),
                )
            )


Example().run()

