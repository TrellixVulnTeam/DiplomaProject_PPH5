import pymongo
from github import Github
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
from pymongo import MongoClient


# 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

# Ddm8ti59QkyxPwqR




class MainApp(MDApp):
    screen = Screen()

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        screen = Builder.load_file('layout.kv')
        return screen

    def set_screen(self, screen):
        self.root.current = screen
        print("switching screen to tokenscreen")

    def clearDB(self):
        client = pymongo.MongoClient(
            "mongodb+srv://radiano2:S4qa9ls4@pycluster.mph6u.mongodb.net/test?retryWrites=true&w=majority")
        db = client["test"]
        db.drop_collection("test")

class TokenScreen(Screen):
    def on_pre_leave(self, *args):
        tokenPassVar = self.ids.tokenFieldID.text

    def set_record(self):
        client = pymongo.MongoClient(
            "mongodb+srv://radiano2:S4qa9ls4@pycluster.mph6u.mongodb.net/test?retryWrites=true&w=majority")
        db = client["test"]
        collection = db["test"]

        post = {"_id": 0, "token": str(self.ids.tokenFieldID.text)}
        collection.insert_one(post)

    pass


class ListScreen(Screen):
    def load_token(self):
        client = pymongo.MongoClient(
            "mongodb+srv://radiano2:S4qa9ls4@pycluster.mph6u.mongodb.net/test?retryWrites=true&w=majority")
        db = client["test"]
        collection = db["test"]

        post = collection.find_one({"_id": 0})

        return post["token"]

    def on_pre_enter(self, *args):
        main_object = MainApp()

        g = Github(self.load_token())

        main_object.clearDB()

        user = g.get_user()
        repos = user.get_repos()
        for x in repos:
            if x.language is not None:
                self.ids.container.add_widget(
                    TwoLineListItem(text=x.name, secondary_text=x.language)
                )

        pass


class RepoScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(TokenScreen(name='tokenscreen'))
sm.add_widget(ListScreen(name='listscreen'))
sm.add_widget(RepoScreen(name='reposcreen'))

if __name__ == '__main__':
    MainApp().run()
