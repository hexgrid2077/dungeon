from data.classes.player_class import Player, equipped_gear, rucksack
from data.classes.player_class import create_starting_inventory
from data.classes.item_class import create_item

player = Player()
create_starting_inventory()
sub_class = "main-hand"

#Equip the axe

equipped_gear["woodsman axe"] = rucksack["woodsman axe"]
player.equip_item("weapon", "main-hand", "woodsman axe")
player.weapon["main-hand"] = create_item("rusty dagger")
player.armor["body"] = create_item("cloth tunic")

player.list_weapons()
print("\nAvailable weapons:")
for key, value in rucksack.items():
    if value.sub_class == "main-hand":
        print(f"{key.title()} x {value.qty}")

print("\nRemoving main-hand weapon...")
player.unequip("weapon", "main-hand")
player.list_weapons()

print("")
print("\nAvailable weapons:")
for key, value in rucksack.items():
    if value.sub_class == "main-hand":
        print(f"{key.title()} x {value.qty}")



weapon_stats = ["atk", "def", "spd", "crit"]
# print(weapon_master)
print("\n PLAYER STATS BEFORE")
player.print_stats()
print("")

weapon_name = "woodsman axe"

# for equip_key, equip_value in equipped_inventory[weapon_name].stats.items():
#     print(f"Equipped Item: {equip_key}: {equip_value}")

#     for player_key, player_value in player.stats.items():
#         print(f"Player Item: {player_key}: {player_value}")
#         if player_key == equip_key:
#             print(f"Adding {equip_value} to {player_key}")
#             player.stats[player_key] = player_value + equip_value
        

print("")
# for key, value in player.stats.items():
#     print(f"{key}: {value}")

print("\n PLAYER STATS AFTER")
player.print_stats()
print("")

# weapon_stats_list = ["atk","def","spd","crit"]
# for stat in weapon_stats_list:
#     player.stats[stat] += equipped_inventory[weapon_name].stats[stat]
#     print(f"{player.stats[stat]} += {equipped_inventory[weapon_name].stats[stat]}")

player.print_stats()
