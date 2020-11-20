from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class ImageList(BoxLayout):
    text = StringProperty()
    source = StringProperty()


class Awaiting(Screen):
    app = MDApp.get_running_app()
    anim = False

    def on_enter(self, *args):
        self.anim = self.app.on_enter("awaiting product", self.anim, self.ids.rv, self.ids.icolabel)
