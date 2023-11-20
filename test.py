from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
import pandas as pd

def index_dataframe(rows):
    d = {}
    df = pd.read_csv('crypto-dataset/Index/Index.csv', index_col=0, nrows=rows)
    for i in df['Symbol']:
        d[i] = "#0ee0e8"
    return d

class MD3Card(MDCard):
    '''Implements a material design v3 card.'''
    pass


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return (
            MDScreen(
                MDBoxLayout(
                    id="box",
                    adaptive_size=True,
                    spacing="56dp",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
            )
        )

    def on_start(self):
        self.root.ids.box.add_widget(
			MD3Card(
				MDRelativeLayout(
					MDIconButton(
						icon="images/logo.png",
						icon_size="50dp",
						pos_hint={"top": 1, "right": 1}
					),
					MDLabel(
						text="first".capitalize(),
						# adaptive_size=True,
						color="#0ee0e8",
						pos=("12dp", "12dp"),
					),
				),
				line_color=(0.2, 0.2, 0.2, 0.8),
				style="elevated",
				padding="4dp",
				size_hint=(None, None),
				size=("250dp", "100dp"),
				md_bg_color="##171717",
				shadow_softness=2 ,
				shadow_offset=(0, 1),
			)
		)

Example().run()