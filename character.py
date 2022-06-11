from kivy.properties import *
from kivy.app import App
from kivy.event import EventDispatcher
import random


class Character(EventDispatcher):
    nick = StringProperty()
    health = NumericProperty()
    strength = NumericProperty()
    agility = NumericProperty()
    stamina = NumericProperty()
    mana = NumericProperty()
    hero_class = StringProperty()
    coins = NumericProperty()

    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)
        self.enemy = App.get_running_app().enemy
        self.nick = ""
        self.health = 100
        self.strength = 5
        self.agility = 5
        self.stamina = 5
        self.mana = 5
        self.hero_class = ""
        self.coins = 100

    def onehanded_attack(self):
        if self.stamina and self.strength and self.agility > 0:
            if self.enemy.e_evade() >= 12:
                self.stamina -= 1
                self.strength -= 1
                self.agility -= 1
                print('enemy evade')
            else:
                self.enemy.e_health -= random.randint(1, self.strength)
                self.stamina -= 1
                self.strength -= 1
                self.agility -= 1
        else:
            print('not enough')

    def twohanded_attack(self):
        if self.stamina and self.strength > 0:
            if self.enemy.e_evade() > 10:
                self.stamina -= 1
                self.strength -= 1
                print('enemy evade')
            else:
                self.enemy.e_health -= random.randint(5, self.strength + 10)
                self.stamina -= 1
                self.strength -= 1
        else:
            print('not enough')

    def ranged_attack(self):
        pass

    def magic_attack(self):
        if self.mana > 0:
            self.enemy.e_health -= random.randint(5, self.mana + 10)
            self.mana -= 1
        else:
            print("not enough mana")



    def evade(self):
        self.luck = random.randint(0, 15 + self.agility)
        self.stamina -= 1
        return self.luck