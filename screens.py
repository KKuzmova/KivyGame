import json
from kivy.app import App
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from hover import HoverBehavior
from sounds import ButtonSound
from kivy.uix.button import Button
from kivy.properties import *
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from tinydb import TinyDB, Query

from kivy.clock import Clock

"""canvas.before:
        Color:
            rgba: (1,1,1,0.7)
        Line:
            width: 1.1
            rectangle: self.x, self.y, self.width, self.height"""

# pot_file = TinyDB('potions.json')
# Pot_item = Query()


class MyToggleButton(ToggleButtonBehavior, Image, RecycleDataViewBehavior):
    selected = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(MyToggleButton, self).__init__(**kwargs)
        self.source = ""

    # def pot_search(self):
    #     pots == pot_file.search(Pot_item.on == self.source)

    def pot_recogniser(self):
        self.icon_image = Image(source=self.source, pos_hint={'x': .28, 'y': .1}, size_hint=(0.13, 0.13))
        App.get_running_app().root.ids.potionsScreen.add_widget(self.icon_image)


    def on_state(self, *l):
        if self.state == 'down':
            self.pot_recogniser()
            self.source = self.source.replace("_off", "_on")
        else:
            App.get_running_app().root.ids.potionsScreen.remove_widget(self.icon_image)
            self.source = self.source.replace("_on", "_off")


class Heading1(HoverBehavior, Label):
    pass


class Heading2(HoverBehavior, Label):
    pass


class Heading3(HoverBehavior, Label):
    pass


class MyRadioBox(HoverBehavior, CheckBox):
    pass


class HoverButton(Button, HoverBehavior, ButtonSound):
    pass


class HoverLabel(Label, HoverBehavior):
    pass


class MenuScreen(Screen):
    pass


class OptionsScreen(Screen):
    pass


class SavesScreen(Screen):
    pass


class ContinueScreen(Screen):
    pass


class CreateNewScreen(Screen, HoverBehavior, ButtonSound):
    character = ObjectProperty()

    check_male = ObjectProperty(None)
    check_female = ObjectProperty(None)
    group = ObjectProperty(None)
    check_human = ObjectProperty(None)
    check_elf = ObjectProperty(None)
    check_beast = ObjectProperty(None)
    check_demon = ObjectProperty(None)
    check_dark_elf = ObjectProperty(None)
    check_orc = ObjectProperty(None)

    check_warrior = ObjectProperty(None)
    check_archer = ObjectProperty(None)
    check_mage = ObjectProperty(None)
    check_rogue = ObjectProperty(None)

    health_stat = ObjectProperty(None)
    agility_stat = ObjectProperty(None)
    strength_stat = ObjectProperty(None)
    stamina_stat = ObjectProperty(None)
    mana_stat = ObjectProperty(None)

    primary = ObjectProperty(None)
    offhand = ObjectProperty(None)
    both_hands = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(CreateNewScreen, self).__init__(*args, **kwargs)
        self.character = App.get_running_app().character

    def check_info(self):
        if self.ids.name_input.text and len(self.ids.name_input.text) <= 16:
            if self.check_male.active or self.check_female.active:
                if self.check_human.active or self.check_elf.active or self.check_beast.active \
                        or self.check_demon.active or self.check_dark_elf.active or self.check_orc.active:
                    if self.check_warrior.active or self.check_archer.active \
                            or self.check_mage.active or self.check_rogue.active:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def get_info(self):
        if self.check_info():
            self.character.nick = self.ids.name_input.text
            self.manager.current = 'Continue'
            self.clear_info()
        else:
            pass

    def ona(self):
        a = self.check_male.get_widgets("gender")
        print(a)
        for b in a:
            if b.active:
                print(b.__dict__)

    def checkbox_stats2(self, value, stat):
        if value.group == "gender":
            if stat == "male":
                self.character.stamina -= 1
                self.character.strength -= 1
            elif stat == "female":
                self.character.agility -= 1
                self.character.mana -= 1
        elif value.group == "race":
            if stat == "elf":
                self.character.health -= 10
                self.character.strength += 2
                self.character.agility -= 1
                self.character.stamina += 2
                self.character.mana -= 2
            elif stat == "beast":
                self.character.health += 30
                self.character.strength -= 2
                self.character.agility -= 1
                self.character.stamina -= 2
                self.character.mana += 2
            elif stat == "demon":
                self.character.health -= 20
                self.character.strength -= 2
                self.character.agility += 4
                self.character.stamina += 2
                self.character.mana -= 2
            elif stat == "dark elf":
                self.character.health += 15
                self.character.strength += 1
                self.character.agility -= 2
                self.character.stamina -= 1
                self.character.mana -= 1
            elif stat == "orc":
                self.character.health -= 15
                self.character.strength -= 3
                self.character.agility += 1
                self.character.stamina -= 1
                self.character.mana += 4
        elif value.group == "class":
            if stat == "warrior":
                self.character.hero_class = ""
                self.primary.text = ""
                self.offhand.text = ""
                self.both_hands.text = ""
                self.character.strength -= 10
                self.character.stamina -= 10
            elif stat == "archer":
                self.character.hero_class = ""
                self.primary.text = ""
                self.offhand.text = ""
                self.both_hands.text = ""
                self.character.agility -= 10
                self.character.stamina -= 10
            elif stat == "mage":
                self.character.hero_class = ""
                self.primary.text = ""
                self.offhand.text = ""
                self.both_hands.text = ""
                self.character.mana -= 10
                self.character.health -= 10
            elif stat == "rogue":
                self.character.hero_class = ""
                self.primary.text = ""
                self.offhand.text = ""
                self.both_hands.text = ""
                self.character.agility -= 10
                self.character.health -= 5
                self.character.mana -= 5

    def checkbox_stats(self, value, stat):

        if value.group == "gender":
            if stat == "male":
                self.character.stamina += 1
                self.character.strength += 1
            elif stat == "female":
                self.character.agility += 1
                self.character.mana += 1
        elif value.group == "race":
            if stat == "elf":
                self.character.health += 10
                self.character.strength -= 2
                self.character.agility += 1
                self.character.stamina -= 2
                self.character.mana += 2
            elif stat == "beast":
                self.character.health -= 30
                self.character.strength += 2
                self.character.agility += 1
                self.character.stamina += 2
                self.character.mana -= 2
            elif stat == "demon":
                self.character.health += 20
                self.character.strength += 2
                self.character.agility -= 4
                self.character.stamina -= 2
                self.character.mana += 2
            elif stat == "dark elf":
                self.character.health -= 15
                self.character.strength -= 1
                self.character.agility += 2
                self.character.stamina += 1
                self.character.mana += 1
            elif stat == "orc":
                self.character.health += 15
                self.character.strength += 3
                self.character.agility -= 1
                self.character.stamina += 1
                self.character.mana -= 4

        elif value.group == "class":
            if stat == "warrior":
                self.character.hero_class = "Warrior"
                self.primary.text = "Sword"
                self.offhand.text = "Shield"
                self.both_hands.text = "Great Sword"
                self.character.strength += 10
                self.character.stamina += 10
            elif stat == "archer":
                self.character.hero_class = "Archer"
                self.primary.text = "Bow"
                self.offhand.text = "Dagger"
                self.both_hands.text = "Sword"
                self.character.agility += 10
                self.character.stamina += 10
            elif stat == "mage":
                self.character.hero_class = "Mage"
                self.primary.text = "Staff"
                self.offhand.text = "Dagger"
                self.both_hands.text = "Sphere"
                self.character.mana += 10
                self.character.health += 10
            elif stat == "rogue":
                self.character.hero_class = "Rogue"
                self.primary.text = "Short Sword"
                self.offhand.text = "Short Sword"
                self.both_hands.text = "Katana"
                self.character.agility += 10
                self.character.health += 5
                self.character.mana += 5

    def clear_info(self):
        self.ids.name_input.text = ""
        self.check_male.active = False
        self.check_female.active = False
        self.check_human.active = False
        self.check_elf.active = False
        self.check_beast.active = False
        self.check_demon.active = False
        self.check_dark_elf.active = False
        self.check_orc.active = False
        self.check_warrior.active = False
        self.check_archer.active = False
        self.check_mage.active = False
        self.check_rogue.active = False


class AdventureScreen(Screen):
    character = ObjectProperty()
    enemy = ObjectProperty()
    pass


class InventoryScreen(Screen):
    pass


class ShopScreen(Screen):
    pass


class SelectStoreScreen(Screen, HoverBehavior):
    def background_change(self, button):
        if button == "armour":
            self.ids.store_background.source = "images/blacksmiths house.png"
        if button == "weapons":
            self.ids.store_background.source = "images/blacksmiths house.png"
        if button == "potions":
            self.ids.store_background.source = "images/magic house.png"
        if button == "accessories":
            self.ids.store_background.source = "images/magic house.png"


class PotionsScreen(Screen):
    # potions = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(PotionsScreen, self).__init__(**kwargs)
        # self.coins = Character.coins
        # print(App.get_running_app().character.coins)
        # self.character = Character()
        # self.data2 = [{'source': img, 'group': 'potions'} for img in
        #               [App.get_running_app().potions['potions']['strength'][i]['off'] for i in
        #                App.get_running_app().potions['potions']['strength']]]
        # for i in self.data2:
        #     i["on_press"] = lambda: self.t(i['source'])
        # print([i['on_press'] for i in self.data2])
        # Clock.schedule_once(lambda dt: self.a())
        # Clock.schedule_once(lambda dt: print(self.potions.data))
        # self.add_widget((source=i, ))
        # print(self.potions.data)

    def maximum_quantity(self):
        pass

    # def a(self):
    #     self.potions.data = self.data2
    #
    # def t(self, *args):
    #     print(self, *args)

    # def sell(self, btn):
    #     if pot not in inventory:
    #         btn.state = 'normal'
    #
    # def buy(self):
    #         self.on_leave()

    def on_leave(self, *args):
        for btn in ToggleButtonBehavior.get_widgets('potions'):
            btn.state = 'normal'


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        LabelBase.register(name='Adventurer',
                           fn_regular='Adventurer.ttf')
