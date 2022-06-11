import screens
import windowPosition
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import json
from character import Character
from enemy import Enemy
from kivy.core.window import WindowBase


class Adventurer(App):
    Window.maximize()

    def __init__(self, **kwargs):
        super(Adventurer, self).__init__(**kwargs)
        with open('potions.json', "r") as file:
            self.potions = json.load(file)
            self.enemy = Enemy('Watcher', 50, 10, 5)
            self.character = Character()


    def build(self):
        kv = Builder.load_file('GameDesign.kv')
        return kv


if __name__ == '__main__':
    Adventurer().run()
