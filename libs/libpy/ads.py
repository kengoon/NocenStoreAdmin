from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class Ads(Screen):
    anim = False
    app = MDApp.get_running_app()

    def on_enter(self, *args):
        self.anim = self.app.on_enter("ads", self.anim, self.ids.swiper, self.ids.icolabel, self.ids.swipe)
