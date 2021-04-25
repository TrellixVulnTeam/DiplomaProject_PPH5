from github import Github
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem


# 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

class MainApp(MDApp):
    screen = Screen()

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        screen = Builder.load_file('layout.kv')
        return screen

    def set_screen(self, screen):
        self.root.current = screen
        print("switching screen to tokenscreen")


g = Github("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 ")
user = g.get_user()  # this line is needed to specify user
repos = user.get_repos()  # array with repos

for x in repos:
    if x.language is not None and x.private == False:
        print("{0} - repo name , {1} - language".format(x.name, x.language))


class TokenScreen(Screen):
    def on_pre_leave(self, *args):
        tokenValue = self.ids.tokenFieldID.text
        print(tokenValue)
    # pass


class ListScreen(Screen):
    def on_pre_enter(self, *args):
        for x in repos:
            if x.language != None:
                self.ids.container.add_widget(
                    TwoLineListItem(text=x.name, secondary_text=x.language)
                )
    # pass


class RepoScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(TokenScreen(name='tokenscreen'))
sm.add_widget(ListScreen(name='listscreen'))
sm.add_widget(RepoScreen(name='reposcreen'))

if __name__ == '__main__':
    MainApp().run()
