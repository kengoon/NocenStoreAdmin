from os import listdir
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineAvatarIconListItem, ImageLeftWidget, IRightBodyTouch
from classes.iconfonts import icon
from classes.m_mdbuttons import M_MDIconButton


class IconRight(IRightBodyTouch, M_MDIconButton):
    pass


class Users(Screen):
    images = listdir("assets/images")
    images.append("")
    app = MDApp.get_running_app()
    anim = False

    def on_enter(self, *args):
        if not self.anim:
            anim3 = Animation(count=5, duration=10) + Animation(count=0, duration=0)
            anim3.repeat = True
            anim3.start(self.ids.product)

        self.anim = self.app.on_enter("users", self.anim, self.ids.app_bar, self.ids.icolabel)
        if not self.ids.content.children:
            for i in range(20):
                user_widget = TwoLineAvatarIconListItem(
                    text=f"[font=assets/ua_scroonge.ttf][color=ffffff]User{i}[/color][/font]",
                    secondary_text=f"[font=assets/ua_scroonge.ttf][color=ffffff][size={int(dp(12))}]offline[/size]"
                                   f"[/color][/font]",
                    divider=None
                )
                user_widget.add_widget(ImageLeftWidget(
                    source="assets/images/user.png",
                    color=self.app.theme_cls.primary_color
                ))
                user_widget.add_widget(IconRight(
                    icon=f"{icon('icon-trash', int(dp(25)), 'ffffff', 'fontello')}"
                ))
                self.ids.content.add_widget(user_widget)

    def change_product(self, count):
        if count != 5:
            self.ids.product.source = f"assets/images/{self.images[int(count)]}"
