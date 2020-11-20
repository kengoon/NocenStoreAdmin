from functools import partial
from os import listdir
from threading import Thread
from kivy.clock import mainthread
from kivy.factory import Factory
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.swiper import MDSwiperItem


class MySwiperSold(MDSwiperItem):
    source = StringProperty()
    text = StringProperty()


class MySwiperBought(MDSwiperItem):
    source = StringProperty()
    text = StringProperty()
    md_bg_color = ListProperty()


class Sold(Screen):
    app = MDApp.get_running_app()
    anim = False

    def on_enter(self, *args):
        self.anim = self.app.on_enter("sold product", self.anim, self.ids.swiper, self.ids.icolabel)
        Thread(target=self.add_sold_product).start()
        Thread(target=self.add_bought_product).start()

    def add_sold_product(self):
        if not len(self.ids.swipe.children[0].children):
            @mainthread
            def add_product(image):
                if not image:
                    self.ids.swipe.add_widget(Factory.LoadMore())
                    return
                self.ids.swipe.add_widget(MySwiperSold(
                    source=f"assets/images/{image}",
                    text="food"
                ))

            images = listdir("assets/images")
            images.append("")
            for i in images:
                Thread(target=partial(add_product, i)).start()

    def add_bought_product(self):
        if not len(self.ids.swipe2.children[0].children):
            @mainthread
            def add_product(image):
                if not image:
                    self.ids.swipe2.add_widget(Factory.LoadMore())
                    return
                self.ids.swipe2.add_widget(MySwiperBought(
                    source=f"assets/images/{image}",
                    text="goat",
                ))

            images = listdir("assets/images")
            images.append("")
            for i in images:
                Thread(target=partial(add_product, i)).start()
