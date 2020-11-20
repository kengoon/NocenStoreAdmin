from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class Notify(Screen):
    anim = False
    app = MDApp.get_running_app()

    def on_enter(self, *args):
        self.anim = self.app.on_enter("notify", self.anim, self.ids.box, self.ids.icolabel)
