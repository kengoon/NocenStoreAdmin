from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.factory import Factory


class Home(Screen):
    app = MDApp.get_running_app()
    index = NumericProperty()

    def go_to(self, item, index):
        self.index = index
        self.app.check_add_screen(
            "libs/main/homemanager.kv", "Factory.HomeManager()", "home manager", "from libs.libpy import homemanager"
        )
        self.check_add_screen(
            f"libs/main/{item}.kv", f"Factory.{item.capitalize()}()", item, f"from libs.libpy import {item}"
        )
        self.manager.current = f"home manager"

    def check_add_screen(self, kv_file, screen_object, screen_name, package):
        if not self.manager.screens[3].ids.manager.has_screen(screen_name):
            exec(package)
            Builder.load_file(kv_file)
            self.manager.screens[3].ids.manager.add_widget(eval(screen_object))
