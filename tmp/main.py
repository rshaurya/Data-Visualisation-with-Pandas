from kivymd.app import MDApp

# Importing builder to use .k`wv file
from kivy.lang import Builder

# Managing screens through screen manager
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('main.kv')

class IntroScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class ScreenTwo(Screen):
    pass

class MainShowScreen(Screen):
    pass

sm = ScreenManager()

# sm.add_widget(IntroScreen(name="intro_screen"))
sm.add_widget(HomeScreen(name="home_screen"))
sm.add_widget(ScreenTwo(name='screen_two'))
sm.add_widget(MainShowScreen(name='main_show_screen'))

class ScreenApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Blue"
        return sm
    
app = ScreenApp()
app.run()
