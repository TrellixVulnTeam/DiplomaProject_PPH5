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
        db.drop_collection("loginCol")

    def repo_switch(self):
        a = MDApp.get_running_app().root.current = 'reposcreen'
        return a


class TokenScreen(Screen):

    def set_token_record(self):
        client = pymongo.MongoClient(
            "mongodb+srv://radiano2:S4qa9ls4@pycluster.mph6u.mongodb.net/test?retryWrites=true&w=majority")
        db = client["test"]
        collection = db["test"]

        post = {"_id": 0, "token": str(self.ids.tokenFieldID.text)}
        collection.insert_one(post)

    def on_pre_enter(self, *args):
        main_object = MainApp()

        main_object.clearDB()


def load_token():
    client = pymongo.MongoClient(
        "mongodb+srv://radiano2:S4qa9ls4@pycluster.mph6u.mongodb.net/test?retryWrites=true&w=majority")
    db = client["test"]
    collection = db["test"]
    collection_login = db["loginCol"]

    if collection.estimated_document_count() != 0:
        post = collection.find_one({"_id": 0})
        return Github(post["token"])
    else:
        post_login = collection_login.find_one({"_id": 0})
        return Github(str(post_login["login"]), str(post_login["password"]))


class ListScreen(Screen):

    def repo_switch(self, screen):
        self.root.current = screen

    def on_pre_enter(self, *args):
        main_object = MainApp()
        list_obejct = ListScreen()
        g = load_token()

        # main_object.clearDB()

        user = g.get_user()
        repos = user.get_repos()

        for x in repos:
            if x.language is not None:
                self.ids.container.add_widget(
                    TwoLineListItem(text=x.name, secondary_text=x.language)
                )

        pass


class RepoScreen(Screen):
    def on_pre_enter(self, *args):
        g = load_token()

        user = g.get_user()
        repo = user.get_repo("DiplomaProject")

        file_content = repo.get_contents("main.py")
        print(file_content.decoded_content.decode())


class LoginScreen(Screen):
    def set_login_record(self):
        client = pymongo.MongoClient(
            "mongodb+srv://radiano2:S4qa9ls4@pycluster.mph6u.mongodb.net/test?retryWrites=true&w=majority")
        db = client["test"]
        collection = db["loginCol"]

        post = {"_id": 0, "login": str(self.ids.loginFieldID.text)
            , "password": str(self.ids.passwordFieldID.text)}

        collection.insert_one(post)


class OptionScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(OptionScreen(name='optionscreen'))
sm.add_widget(TokenScreen(name='tokenscreen'))
sm.add_widget(ListScreen(name='listscreen'))
sm.add_widget(RepoScreen(name='reposcreen'))
sm.add_widget(LoginScreen(name='loginscreen'))

if __name__ == '__main__':
    MainApp().run()
