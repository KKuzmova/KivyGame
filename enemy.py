from kivy.properties import *
from kivy.event import EventDispatcher
from kivy.app import App
import random


class Enemy(EventDispatcher):
    e_name = StringProperty()
    e_health = BoundedNumericProperty(0, min=0, max=500, errorvalue=0)
    e_strength = NumericProperty()

    def __init__(self, e_name, e_health, e_strength, e_agility, *args, **kwargs):
        super(Enemy, self).__init__(*args, **kwargs)
        # self.character = App.get_running_app().character
        self.e_name = e_name
        self.e_health = e_health
        self.e_strength = e_strength
        self.e_agility = e_agility

    # def attack(self):
    #     if self.character.evade() > 10 - self.character.agility:
    #         print('character evade')
    #     else:
    #         self.character.health -= random.randint(0, self.e_strength + 5)

    def e_evade(self):
        self.e_luck = random.randint(0, 12)
        return self.e_luck

