from data.data_files.signs import dungeon_title, divider
from data.maps.crypt import locations, exit_location
from data.npc_dialog import say_something_random
from engine_room.loot_menu import show_location_items
from engine_room.inventory_menu import show_inventory
from rich.console import Console
from data.maps.map_class import Game_Map
from data.classes.battle_class import Battle
from data.classes.player_class import Player
from data.classes.enemy_class import Enemy
from data.classes.enemy_class import create_enemy
from data.classes.item_class import Item
from data.data_files.config import hud_theme
from random import randint
from time import sleep

console = Console(theme=hud_theme, highlight=False)

def move(current_location, change, player):
    new_location = (current_location[0]+change[0],current_location[1]+change[1])
    if new_location in locations:
        current_location = new_location
        
        check_random_enemies(current_location, player)
        locations[current_location]["visited"] = "y"
        return current_location
    else:
        console.print("\n\nYou can't go this way.", style="exit")
        return current_location

def game_over():
    while True:
        console.print("GAME OVER...\n", style="loot")
        print("Load past save?")
        console.print("Press [b]ENTER[/] to load save game.", style="menu")
        choice = input("")
        if choice == '': break
        else: break


def check_random_enemies(current_location, player):
    enemies_in_location_dict = locations[(current_location)]["enemies"]
    draw = randint(1,100)
    for key, value in enemies_in_location_dict.items():
        if int(key[0]) <= draw <= int(key[1]):
            enemy = value
    if enemy != "clear":
        while player.is_alive():
            enemy = create_enemy(enemy)
            battle = Battle(enemy, player)
            battle.loop(player, enemy)
        else:
            console.print("\nYOU ARE DEAD!", style="enemy")

def show_exits(movement, current_location):
    console.print("[exit]Exits:[/] ",end="")
    exit_list = []
    exit_list.clear()
    if ((movement['n'][0]+current_location[0]),(movement['n'][1]+current_location[1])) in locations: exit_list.append("[b]n[/]orth")
    if ((movement['e'][0]+current_location[0]),(movement['e'][1]+current_location[1])) in locations: exit_list.append("[b]e[/]ast")
    if ((movement['s'][0]+current_location[0]),(movement['s'][1]+current_location[1])) in locations: exit_list.append("[b]s[/]outh")
    if ((movement['w'][0]+current_location[0]),(movement['w'][1]+current_location[1])) in locations: exit_list.append("[b]w[/]est")
    for exit in exit_list: console.print(f"{exit} ",end="", style="exit")

def status(player):
    while True:
        player.print_stats()
        console.print("Press [b]ENTER[/] to continue", style="menu")
        choice = input("")
        if choice == '': break
        else: break

def show_map(current_location, exit_location):
    while True:
        game_map = Game_Map(locations, current_location, exit_location)
        console.print("Press [b]ENTER[/] to continue", style="menu")
        choice = input("")
        if choice == '': break
        else:break

def display_scene(current_location):
    console.print(f"\n\n{locations[(current_location)]["description"]}")
    if locations[(current_location)]["name"] == "crypt" and locations[current_location]["visited"] == "n": 
        console.print(f"{say_something_random()}")

def scan_area(current_location, player):
     console.print("\n---------------\nITEMS AVAILABLE\n")
     if len(locations[current_location]["items"]) == 0:
         console.print("NO ITEMS FOUND")
         display_scene(current_location)
     else:
          show_location_items(current_location, locations, player)


def prompt(current_location, player):
    movement = {"n": ((current_location[0]+0),(current_location[1]+1)), "e": ((current_location[0]+1),(current_location[1]+0)), 
                "s": ((current_location[0]+0),(current_location[1]-1)), "w": ((current_location[0]-1),(current_location[1]+0)),
                "north": ((current_location[0]+0),(current_location[1]+1)), "east": ((current_location[0]+1),(current_location[1]+0)), 
                "south": ((current_location[0]+0),(current_location[1]-1)), "west": ((current_location[0]-1),(current_location[1]+0))}
    
    while player.is_alive():
        display_scene(current_location)
        console.print(f"\nHP [stat]{player.hp}[/]/[stat]{player.max_hp}[/]\tMP [stat]{player.mp}[/]/[stat]{player.max_mp}[/]", style="hp-mp")
        console.print("[b u]I[/]nventory | Scan [b u]A[/]rea | S[b u]t[/]atus | [b u]M[/]ap | Sa[b u]v[/]e/Load", style="menu")
        show_exits(movement, current_location)
        console.print("\n> ", style="prompt",end='')

        non_move_choices = {"i": show_inventory, #(player)
                            "a": scan_area, #(current_location)
                            "t": status,
                            "m": show_map,}
        try:
            choice = input("").lower()
            if choice in movement:
                current_location = move(current_location, movement.get(choice), player); sleep(0.3)
            if choice in non_move_choices:
                if choice == "i": sleep(0.3); show_inventory(player)
                if choice == "a": sleep(0.3); scan_area(current_location, player)
                if choice == "t": sleep(0.3); status(player)
                if choice == "m": sleep(0.3); show_map(current_location, exit_location)
            else:
                pass
        except KeyError:
            pass
    else:
        game_over()


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


def initialize():
    console.print(dungeon_title, style="attacked")
    player = Player()
    create_starting_inventory(player)
    curr_loc = (0,0) # Starting location
    prompt(curr_loc,player)