from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

from classes.iconfonts import icon

app = MDApp.get_running_app()


class HomeManager(Screen):
    bottomnavigation_items = [
        {
            "icon": f"{icon('icon-googleads', int(dp(25)), '4384f4', 'icomoon')}", 'text': 'ads',
            'on_release': lambda x: HomeManager.transit(app.root.screens[3], "ads", "up"),
            "font_name": "assets/ua_scroonge.ttf"
        },
        {
            "icon": f"{icon('icon-users', int(dp(25)), '45459a', 'fontello')}", 'text': 'users',
            'on_release': lambda x: HomeManager.transit(app.root.screens[3], "users", "down"),
            "font_name": "assets/ua_scroonge.ttf"
        },
        {
            "icon": f"{icon('icon-marketo', int(dp(25)), '424242', 'icomoon')}", 'text': 'sold',
            'on_release': lambda x: HomeManager.transit(app.root.screens[3], "sold", "left"),
            "font_name": "assets/ua_scroonge.ttf"
        },
        {
            "icon": f"{icon('icon-floatplane', int(dp(25)), '42c531', 'icomoon')}", 'text': 'awaiting',
            'on_release': lambda x: HomeManager.transit(app.root.screens[3], "awaiting", "right"),
            "font_name": "assets/ua_scroonge.ttf"
        },
        {
            "icon": f"{icon('icon-bell', int(dp(25)), 'f03727', 'fontello')}", 'text': 'notify',
            'on_release': lambda x: HomeManager.transit(app.root.screens[3], "notify", "up"),
            "font_name": "assets/ua_scroonge.ttf"
        },
        {
            "icon": f"{icon('icon-off', int(dp(25)), 'f03727', 'fontello')}", 'text': 'shutdown',
            'on_release': lambda x: HomeManager.transit(app.root.screens[3], "shutdown", "down"),
            "font_name": "assets/ua_scroonge.ttf"
        }
    ]

    def transit(self, *args):
        self.manager.screens[2].check_add_screen(
            f"libs/main/{args[0]}.kv", f"Factory.{args[0].capitalize()}()", args[0], f"from libs.libpy import {args[0]}"
        )
        self.ids.manager.transition.direction = args[1]
        self.ids.manager.current = args[0]

    def on_enter(self, *args):
        self.ids.bottom_navigation.set_current(self.manager.screens[2].index)
        self.ids.bottom_navigation.ids._buttons_bar.children[self.manager.screens[2].index].dispatch("on_release")
