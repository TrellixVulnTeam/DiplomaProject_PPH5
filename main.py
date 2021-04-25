from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.lang import Builder
from github import Github
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, OneLineListItem, TwoLineListItem
from kivy.lang import Builder
from kivy.properties import StringProperty

# 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
g = Github("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")
user = g.get_user() # this line is needed to specify user
repos = user.get_repos() # array with repos

for x in repos:
    if x.language != None and x.private == False:
        print("{0} - repo name , {1} - language".format(x.name,x.language))



class MainApp(MDApp):
    screen = Screen()
    scr_mngr = ObjectProperty(None)
    tokenscreen = ObjectProperty(None)

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        screen = Builder.load_file('layout.kv')
        return screen

    def set_screen(self, screen):
        self.root.current = screen
        print("switching screen to tokenscreen")

    # def on_start(self):
    #     tokenValue = self.scr_mngr.tokenscreen.tokenfield.text
    #     g = Github(tokenValue)
    #     user = g.get_user()
    #     repos = user.get_repos()


class TokenScreen(Screen):
    # def getToken(self):
    #     tokenValue = self.scr_mng.tokenID.tokenfield.text
    #     g = Github(tokenValue)
    #     user = g.get_user("radiano2")
    #     repos = user.get_repos()
    pass


class ListScreen(Screen):

    def on_pre_enter(self, *args):

        for x in repos:
            if x.language != None:
                self.ids.container.add_widget(
                    TwoLineListItem(text=x.name, secondary_text=x.language)
                )


class RepoScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(TokenScreen(name='tokenscreen'))
sm.add_widget(ListScreen(name='listscreen'))
sm.add_widget(RepoScreen(name='reposcreen'))

if __name__ == '__main__':
    MainApp().run()
