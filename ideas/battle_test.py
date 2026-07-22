from data.maps.crypt import locations
from data.npc_dialog import say_something_random
from engine_room.loot_menu import show_location_items
from engine_room.inventory_menu import show_inventory
from rich.console import Console
from data.classes.battle_class import Battle
from data.classes.player_class import Player
from data.classes.enemy_class import Enemy
from data.classes.enemy_class import create_enemy
from data.classes.item_class import Item
from data.data_files.config import hud_theme


from data.classes.player_class import Player, rucksack, equipped_gear
from data.classes.battle_class import Battle
from data.classes.item_class import Item, Consumable
from data.classes.enemy_class import create_enemy


player = Player()
wraith = create_enemy("wraith")
battle = Battle(wraith, player)


def create_starting_inventory(player):
        from data.item_master import starting_equipment, starting_items

        for entry in starting_items:
            new_item = Item.create_item(Item, entry[0])
            new_item.qty = entry[1]
            player.rucksack[new_item.name] = new_item

        for entry in starting_equipment:
            new_item = Item.create_item(Item, entry[0])
            new_item.qty = entry[1]
            player.equipped_gear[new_item.name] = new_item
        for name, obj in player.equipped_gear.items():
            player.equip_item(obj.item_class.lower(), obj.sub_class, name)

create_starting_inventory(player)


# battle.loop(player, wraith)

battle.player_attack_roll(player, wraith)

# for item, qty in player.rucksack.items():
#     print(item, qty)

