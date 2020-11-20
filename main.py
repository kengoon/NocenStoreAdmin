from functools import partial
from threading import Thread
from time import sleep

from akivymd.uix.statusbarcolor import change_statusbar_color
from kivy import platform
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp
from pyrebase import pyrebase

from classes.a_bottomnavigation import M_AKBottomNavigation
from classes.a_silverappbar import M_AKSilverAppbar
from classes.card import MsCard
from classes.iconfonts import register

register('fontello', 'assets/fontello.ttf', 'assets/fontello.fontd')
register("icomoon", "assets/icomoon.ttf", "assets/icomoon.fontd")
register("icomoon2", "assets/icomoon2.ttf", "assets/icomoon2.fontd")
r = Factory.register
r("CircularElevationBehavior", module="kivymd.uix.behaviors.elevation")
r("CircularRippleBehavior", module="kivymd.uix.behaviors.ripplebehavior")
r("RectangularElevationBehavior", module="kivymd.uix.behaviors.elevation")
r("RectangularRippleBehavior", module="kivymd.uix.behaviors.ripplebehavior")

if platform == 'android':
    from android.permissions import request_permissions, Permission

    request_permissions([
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.READ_EXTERNAL_STORAGE,
        Permission.INTERNET,
        Permission.CALL_PHONE,
        Permission.CALL_PRIVILEGED
    ])
r = Factory.register
r("MsCard", cls=MsCard)
r("M_AKBottomNavigation", cls=M_AKBottomNavigation)
r("M_AKSilverAppbar", cls=M_AKSilverAppbar)

# firebase credentials
cred = {
    "type": "service_account",
    "project_id": "nocenstore-da771",
    "private_key_id": "85ac6b7b2cf7f9bf06c1bd9aacacf9e95a62d2a4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCoVnbR3NRG4Cxx"
                   "\nupCsPub2/hNJZMWSHeUAZOx0JocdA+0D3MQQIfu40q4Be2BLVrZy09PpUZMA85Ga"
                   "\nOM70dshqhBPIkRTYYCwpmkmQWXhvgnjyGmvu6BySDju0y4rNlZNe2oHrHmk5cU+E\nEVJKfIfLT6BFdYTzy"
                   "/OiC6E9z9UcwsFFbirpkYdTE+GKRn9oYSyKBjXcPhQBfh+P\niiOC/muIKz7TdV3Pd+fWk+ljcvKGok"
                   "++XNQYyqSQjYv30VG8J8w/yWSvpRgF6vSV\nXWMdXa401eUe/Jlzx/rEc2ziblOyflpKkVBsOnLfZ61NPi1K"
                   "+5xV1zZcMbYO7a2m\nHsjW2lmpAgMBAAECggEAUk8ovPeRkfA1uwwihh4hl55m9sl/szDL0rQGS8q04PKU"
                   "\n9wEAmvTK3LWi4FWfoWbOQfoiUSCSVPJDfNmPE8hquW5IMBcETsJDhboLgznEIh31\nHkfeA4xZv+6WshGeFmSvEL"
                   "+dq8WMZMprO2OuzX3zde1CrAPI1N4iC9dM6WjQRsWG\nXliCiACXUdB1uHfNScAhoZ1Oe"
                   "/hVl2MRYBd38xEdJtrlNuIsbWskiQvuh9VtgLnz\nGjSctmPgj4f4aK60hlc2O1lSN/ThREQHuOvtLw38oscegz7C"
                   "+k4mWTR8l1mHPbDt\nAKMv/bfdnejN5u/BCuP/pA70bxt1uNtsOr3zHjaaGwKBgQDVWS8ZWgBAtEF8glea\nRn9ti04BTk"
                   "/991mW0bfTGerPnG1yrWA83rf3gSPGHatpCLRnULo7cp4rg8RUkqvg\nnA1e3K9a"
                   "+MwaNWzgdJbQfjWv8SCPx98DlD1YbhsxXrI3ITHy3GNXBk2eIzHNdDXg\nog2ltZzSestES6QvZRsxHA3l1wKBgQDJ"
                   "/bYHNQU6YNBYYI3DmkFMUxIciaAeNug9\nabhBBw5wQgFLh4YgA1LIcJCIONmJkAVCxPbHpdJNeaubJaxxysetg3G+UiSTmdia"
                   "\n1ktHg6k9bjcWK1KAh8VEcexyr+qaKsqquWvjGArmBFe/sc9JcnsebA5Ns+uWrlO6\n8boTd"
                   "+LMfwKBgCiiPcg0TgwEyNwv7wNhHe/9MjQpeC7Ep3mEI+C+9OvpvSa0QroV"
                   "\nKTColemryPPORp3O0El2QQ3EoOYCsV2sGxfQLE3FSQpM1pnBWuAGya7i2/LGfIEw"
                   "\nAKcRAXjbslGxrtO0ie8PMkVGKrwYwBIyiyredinYXVJ6naCxPwaRc0wtAoGBAIoJ"
                   "\no4MLXdZGYTt0SI069pLlVkRAXTcoyM9nVy7BVsGqqd3m8OchvkoSewNM7oUO8jlu"
                   "\nB0Pq82xU0MyHE3D0Zj8SzAGHe02PXrJ57hoiRN8hWe4BjzEdF9etjyvVQps20SeY\n7bzVKmWE5D6xkfocjTz"
                   "+FUxOv5pK6hegqEwzqr+bAoGAeIMW+wx0jYCiok7u8NWb\nc0A7ZVxGLmaMbvPKb4jeiHi84BI1+YOhz/EBzL"
                   "/mR2jFJmOJqZzgfDUyFPxkFD+J\nguAo6POspHPG/EopWAOSksPLdxESAVvihgszlC2XG77GG4yzgqrE00hbw6uXFl3O"
                   "\nCvss3ZWtWVcvfdFgLYvdz5A=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-xroe4@nocenstore-da771.iam.gserviceaccount.com",
    "client_id": "110770762460776752017",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xroe4%40nocenstore"
                            "-da771.iam.gserviceaccount.com "
}
config = {
    "apiKey": "AIzaSyAmFfBwmXiEBdnMsgB1MGmdApe5A7eUMc8",
    "authDomain": "nocenstore-da771.firebaseapp.com",
    "databaseURL": "https://nocenstore-da771.firebaseio.com",
    "projectId": "nocenstore-da771",
    "storageBucket": "nocenstore-da771.appspot.com",
    "messagingSenderId": "565612115920",
    "appId": "1:565612115920:web:32777df7039a2e23ff2bd5",
    "measurementId": "G-1QSNCDR7HC",
    "serviceAccount": cred
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
storage = firebase.storage()


class NocenStoreAdmin(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Green"
        Window.softinput_mode = 'below_target'
        change_statusbar_color(self.theme_cls.primary_color)

    def build(self):
        kv_dirs = "libs"
        exec("from libs.libpy import serverinit")
        Builder.load_file(f"{kv_dirs}/init/initiate_server.kv")
        return Builder.load_file(f"{kv_dirs}/manager.kv")

    def on_start(self):
        anim = Animation(p=4, d=2, t="linear") + Animation(p=0, duration=0, t="linear")
        anim.repeat = True
        anim.start(self.root.screens[0].ids.spinner)
        Thread(target=partial(self._connect_server, anim)).start()

    def _connect_server(self, anim):
        sleep(5)
        self.check_add_screen("libs/init/login.kv", "Factory.Login()", "login", "from libs.libpy import login")
        anim.stop(self.root.screens[0].ids.spinner)
        self.root.current = "login"

    def check_add_screen(self, kv_file, screen_object, screen_name, package):
        if not self.root.has_screen(screen_name):
            exec(package)
            Builder.load_file(kv_file)
            self.root.add_widget(eval(screen_object))

    def on_enter(self, screen, animation, root, label, instance=None):
        self.root.screens[3].ids.toolbar_name.text = screen
        if not animation:
            def anim2(*all):
                Animation(opacity=1, duration=1).start(root)
                instance.set_current(1) if instance else None

            anim = Animation(opacity=0, duration=1)
            anim.bind(on_complete=anim2)
            anim.start(label)
            return True


if __name__ == '__main__':
    NocenStoreAdmin().run()
