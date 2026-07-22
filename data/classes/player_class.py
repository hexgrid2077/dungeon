
# from data.classes.item_class import Item
from rich.console import Console
from rich.table import Table
from data.classes.item_class import Item
from data.data_files.config import hud_theme
from engine_room.inventory_menu import print_equipped_items


console = Console(theme=hud_theme, highlight=False)
rucksack = {}
equipped_gear = {}


class Player:
    def __init__(self, hp=50,max_hp=50, mp=30, max_mp=50, armor=None, weapon=None, exp=0, inventory={}, equipped={}, stats=None, status=None):
        self.hp = 100
        self.max_hp = 100
        self.mp = 30
        self.max_mp = 30
        self.armor = {"head":None,"body":None,"hands":None,"feet":None,}
        self.weapon = {"main-hand":None,"off-hand":None,}
        self.exp = exp
        self.rucksack = rucksack
        self.equipped_gear = equipped_gear
        self.stats = {"atk":10,"def":0,"dex":10,"int":10,"crit":5,}
        self.status = "Healthy"
        self.resist = None


    def print_stats(self):
        console.print("\n[b]STATUS[/]\n", style="menu")
        status_table = Table(box=None, show_header=True, show_footer=False, padding=0, title_justify="left")
        status_table.add_column("[armor]Category[/]", width=10)
        status_table.add_column("[armor]Points[/]", width=10, justify="center")

        for stat, value in self.stats.items():
            status_table.add_row(f"[grayed]{stat.upper()}[/]", f"{value}")
        status_table.add_row(f"[grayed]Resist:[/]", f"{self.resist}")
        status_table.add_row(f"[grayed]Status:[/]", f"{self.status}")
        status_table.add_row(f"[loot]GOLD[/]", f"{self.rucksack["gold"].qty}")
        console.print(status_table)
        print("")


    def is_alive(self):
        if self.hp > 0:
            return True      


    def equip_item(self, weap_armor, sub_class, item_name):
        #TODO make this move the item to equipped inventory rather than the inventory menu doing it.
        if weap_armor == "weapon":
            self.weapon[sub_class] = equipped_gear[item_name]
        elif weap_armor == "armor":
            self.armor[sub_class] = equipped_gear[item_name]
            
        # Add stats from item to player
        for equip_key, equip_value in equipped_gear[item_name].stats.items():
            for player_key, player_value in self.stats.items():
                if player_key == equip_key:
                    self.stats[player_key] = player_value + equip_value


    def unequip(self, weap_armor, sub_class):
        if weap_armor == "weapon":
            item_name = self.weapon[sub_class].name
            self.weapon[sub_class] = None
        elif weap_armor == "armor":
            item_name = self.armor[sub_class].name
            self.armor[sub_class] = None

        if item_name in rucksack:
            rucksack[item_name].qty += 1
        else:
            rucksack[item_name] = Item.create_item(Item, item_name)
        
        print(f"{item_name.title()} removed...")
        # Add stats from item to player
        for equip_key, equip_value in equipped_gear[item_name].stats.items():
            for player_key, player_value in self.stats.items():
                if player_key == equip_key:
                    self.stats[player_key] = player_value - equip_value


    def transfer_to_equipped(self, sub_class, weapon_or_armor):
            temp_option_list = []
            for key, value in self.rucksack.items():
                if value.sub_class == sub_class:
                    temp_option_list.append(key)
            # Print enumerated temp list
            console.print(f"\n{sub_class.title()} Options:", style="submenu")
            numerated_list = list(enumerate(temp_option_list))
            for option in numerated_list:
                console.print(f"{option[0]+1}) {option[1].title()}")
            console.print("\nChoose Number:", style="submenu")
            console.print("> ", style="prompt",end='')
            try:
                class_equip_choice = int(input(""))
            except ValueError:
                print_equipped_items(self)
            try:
                item_name = numerated_list[class_equip_choice-1][1]
                # Keep note of original player inventory qty so we can update it below
                orig_item_qty = self.rucksack[item_name].qty
                # Move that item x1 to the equipped inventory
                self.equipped_gear[item_name] = self.rucksack[item_name]
                self.equipped_gear[item_name].qty = 1
                # Adjust player inventory qty by 1 or delete if it is 0
                if orig_item_qty > 1:
                    self.rucksack[item_name].qty -=  1
                else:
                    del self.rucksack[item_name]
                # Equip the item and unequip anything existing.
                if weapon_or_armor == "weapon":
                    if self.weapon[sub_class] == None:
                        self.equip_item(weapon_or_armor, sub_class, item_name)
                    else:
                        self.unequip(weapon_or_armor, sub_class)
                        self.equip_item(weapon_or_armor, sub_class, item_name)
                elif weapon_or_armor == "armor":
                    if self.armor[sub_class] == None:
                        self.equip_item(weapon_or_armor, sub_class, item_name)
                    else:
                        self.unequip(weapon_or_armor, sub_class)
                        self.equip_item(weapon_or_armor, sub_class, item_name)
                        
                print_equipped_items(self)
            except IndexError:
                print_equipped_items(self)


    def use_item(self, item):
        add_hp = self.rucksack[item].stats["hp"]
        add_mp = self.rucksack[item].stats["mp"]
        self.hp += add_hp
        self.mp += add_mp

        # Ensure you cannot exceed the max
        if self.hp > self.max_hp: self.hp = self.max_hp
        self.mp += self.mp
        if self.mp > self.max_mp: self.mp = self.max_mp
        print(f"Drank {item} yielding {self.rucksack[item].stats["hp"]} hp and {self.rucksack[item].stats["mp"]} mp.")

        # Reduce the qty of item
        if self.rucksack[item].qty > 1:
            self.rucksack[item].qty -= 1
            return            
        else:
            del self.rucksack[item]


