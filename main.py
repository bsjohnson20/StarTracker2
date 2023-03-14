import kivymd.uix.button
from kivy import app
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.label import MDLabel


# setup device storage
from kivy.storage.jsonstore import JsonStore

devices = JsonStore("devices.json")
setTheme = JsonStore("theme.json")
storedThemes = JsonStore("themes.json")


class UsefulToolbar(
    BoxLayout):  # make a consistent toolbar, like the one you truely want. I mean it. I really know you want it.
    def __init__(self, prim_text="Back", sec_text="Title", thir_text="Settings", **kwargs, ):
        super(UsefulToolbar, self).__init__(**kwargs)


class Title(MDLabel):
    def __init__(self, **kwargs):
        super(Title, self).__init__(**kwargs)
        self.font_style = "H6"
        self.theme_text_color = "Custom"
        self.text_color = (0, 0, 0, 1)
        self.halign = "center"
        self.valign = "middle"


class MainScreen(Screen):
    pass


# first triple screen set
class HomeScreen(Screen):
    pass


class AddDeviceScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class DevicePage(Screen):
    pass


class DeviceSettings(Screen):
    pass


class ScreenManagement(ScreenManager):
    last_screen = StringProperty()

    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        self.transition = FadeTransition()
        self.last_screen = "main"


class MainApp(MDApp):
    def build(self):
        # theme
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        return Builder.load_file("screens/main.kv")


MainApp().run()
