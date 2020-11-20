from functools import partial
from threading import Thread
from time import sleep
from classes.a_bottomnavigation import M_AKBottomNavigation
from classes.a_silverappbar import M_AKSilverAppbar
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.factory import Factory
from akivymd.uix.statusbarcolor import change_statusbar_color
from kivy import platform
from kivymd.app import MDApp
from kivy.lang import Builder
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
