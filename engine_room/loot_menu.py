from data.classes.player_class import rucksack, Player
from data.classes.item_class import Item
from rich.console import Console
from data.data_files.config import hud_theme


console = Console(theme=hud_theme, highlight=False)


def show_location_items(current_location, locations, player): # Makes an enumerated list of the item dictionary in that location
    location_items_dict = locations[current_location]["items"]
    
    while True:
        for i, (item, qty) in enumerate(location_items_dict.items()):
            console.print(f"{i+1}) {item.title()} x {qty}")
        if len(location_items_dict) == 0:
            break        
        take_choice = input(f"\nWhich item(s) do you want to take?\nItem # | (A)ll | (B)ack: ").lower()
        if take_choice == "a":
            console.print("\nYou take all the items")
            take_all(location_items_dict, player)
            break
        elif take_choice == "b":
            break
        elif not take_choice.isnumeric():
            pass
        elif int(take_choice) in range(1,9):
            take_single_item(player, location_items_dict, int(take_choice))


def take_all(location_items, player):
    for item,qty in location_items.items():
        if item in player.rucksack:
            player.rucksack[item].qty += qty
        else:
            new_item = Item.create_item(Item, item)
            new_item.qty = qty
            player.rucksack[new_item.name] = new_item
            
    # Remove the items from the location dictionary
    temp_key_list = list(location_items.keys())
    for key in temp_key_list:
        del location_items[key]


def take_single_item(player, location_items_dict, take_choice):
    take_choice -= 1 # Shift back to starting at 0.
    available_items = (list(enumerate(location_items_dict.items())))
    req_item_name = available_items[take_choice][1][0]
    available_item_qty = available_items[take_choice][1][1]
    req_item_qty = int(input(f"\nHow many {req_item_name}? "))

    # If the items are there, take them
    if ensure_qty_is_available(available_item_qty, req_item_qty, req_item_name) == True:
        add_to_player_inventory(player, req_item_name, req_item_qty)
        remove_from_location_inventory(location_items_dict, req_item_qty, req_item_name, available_item_qty)       


def ensure_qty_is_available(available_item_qty, req_item_qty, req_item_name):
    if available_item_qty >= req_item_qty:
        return True
    else:
        console.print(f"\nThere is not enough {req_item_name}.\n")
        return False


def add_to_player_inventory(player, req_item_name, req_item_qty):
    console.print(f"Transfering: {req_item_name} x {req_item_qty}\n")
    if req_item_name in player.rucksack:
        player.rucksack[req_item_name].qty += req_item_qty
    else:
        new_item = Item.create_item(req_item_name)
        new_item.qty = req_item_qty
        player.rucksack[new_item.name] = new_item


def remove_from_location_inventory(location_items_dict, req_item_qty, req_item_name, available_item_qty):
    if available_item_qty >= req_item_qty:
        remaining_loc_item_qty = available_item_qty - req_item_qty     
        location_items_dict[req_item_name] = remaining_loc_item_qty

        # If item is zero, remove from the location dictionary
        if location_items_dict[req_item_name] == 0:
            del location_items_dict[req_item_name]