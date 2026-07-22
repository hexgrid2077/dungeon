
from data.item_master import *

class Item:
    def __init__(self, name, item_class, sub_class, description, stats=None, price=None, qty=1):
        self.name = name
        self.item_class = item_class
        self.sub_class = sub_class
        self.description = description
        self.stats = stats
        self.price = price
        self.qty = qty

    def setup_weapon_armor_consumable_object(item, classname, masterlist):
        item = classname(
             item,
             masterlist[item]["item_class"],
             masterlist[item]["sub_class"],
             masterlist[item]["description"],
             masterlist[item]["stats"],
             masterlist[item]["price"],)
        return item

    def setup_quest_object(item, classname, masterlist):
        item = classname(
            item,
            masterlist[item]["item_class"],
            masterlist[item]["sub_class"],
            masterlist[item]["description"],
            masterlist[item]["quest"],)
        return item

    def create_item(self, item):
        master_dicts = [consumable_master, weapon_master, armor_master, quest_master]
        
        class_map = {
        "Consumable":{"classname": Consumable,"masterlist": consumable_master},
        "Weapon":{"classname": Weapon,"masterlist": weapon_master},
        "Armor":{"classname": Armor,"masterlist": armor_master},
        "Quest":{"classname": Quest,"masterlist": quest_master},}

        for master_dict in master_dicts:
            if item in master_dict:
                class_string = master_dict[item]["item_class"]
                classname = class_map[class_string]["classname"]
                masterlist = master_dict
                if class_string == "Quest":
                    return self.setup_quest_object(item, classname, masterlist)
                else:
                    return self.setup_weapon_armor_consumable_object(item, classname, masterlist)

class Weapon(Item):
        ...       

class Armor(Item):
        ...

class Consumable(Item):
    def __init__(self, name, item_class, sub_class, description, stats=None, price=None, qty=1):
         super().__init__(name, item_class, sub_class, description, stats, price, qty)

class Quest(Item):
    def __init__(self, name, item_class, sub_class, description, quest, qty=1):
        super().__init__(name, item_class, sub_class, description, qty) # What we're taking from the main Item class (notice quest is not here)
        self.quest = quest

    def view(self):
        print(f"Name: {self.name.title()}")
        print(f"Item Class: {self.item_class}")
        print(f"Sub Class: {self.sub_class}")
        print(f"Description: {self.description}")
        print(f"Quest: {self.quest}")






