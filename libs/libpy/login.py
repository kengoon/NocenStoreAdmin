from functools import partial
from os import listdir
from threading import Thread

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_custom_kv_classes()

    def build_custom_kv_classes(self):
        for classFiles in listdir("libs/classes"):
            Thread(target=partial(self.thread_build_kv, classFiles)).start()

    @staticmethod
    def thread_build_kv(classFiles):
        Builder.load_file(f"libs/classes/{classFiles}")
