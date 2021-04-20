from kivy.lang import Builder
from kivy.properties import StringProperty
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

g = Github("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 ")

user = g.get_user("radiano2")

repos = user.get_repos()


class TokenScreen(Screen):
    pass


class ListScreen(Screen):
    def on_pre_enter(self, *args):
        # for x in repos:
        #     if x.language != None:
        #         self.ids.container.add_widget(
        #             OneLineListItem(text="{0} - {1}".format(x.name, x.language))
        #         )
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


class MainApp(MDApp):
    screen = Screen()

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        screen = Builder.load_file('layout.kv')
        return screen

    def set_screen(self, screen):
        self.root.current = screen
        print("switching screen to tokenscreen")


if __name__ == '__main__':
    MainApp().run()
