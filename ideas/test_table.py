from data.classes.player_class import Player
player = Player()


from rich.console import Console
from rich.table import Table
console = Console()

weapon_table = Table(title="WEAPONS", box=None, show_header=True, show_footer=False, padding=0)
weapon_table.add_column("Slot", width=15)
weapon_table.add_column("Weapon", width=20)
weapon_table.add_column("ATK", width=10, justify="center")
weapon_table.add_column("SPD", width=10, justify="center")
weapon_table.add_column("CRIT", width=10, justify="center")

for slot, item in player.weapon.items():
    if item != None:
        weapon_table.add_row(f"{slot.title()}", f"{item.name.title()}", f"{item.stats["atk"]}",\
                                    f"{item.stats["spd"]}", f"{item.stats["crit"]}")
    else:
        weapon_table.add_row(f"{slot.title()}", f"Not Equipped")


armor_table = Table(title="ARMOR", box=None, show_header=True, show_footer=False, padding=0)
armor_table.add_column("Slot", width=15)
armor_table.add_column("Armor", width=20)
armor_table.add_column("DEF", width=10, justify="center")
armor_table.add_column("SPD", width=10, justify="center")
armor_table.add_column("RESIST", width=10, justify="center")

for slot, item in player.armor.items():
    if item != None:
        armor_table.add_row(f"{slot.title()}", f"{item.name.title()}", f"{item.stats["def"]}",\
                                    f"{item.stats["spd"]}", f"{item.stats["resist"]}")
    else:
        armor_table.add_row(f"{slot.title()}", f"Not Equipped")

print("")
console.print(weapon_table)
print("")
console.print(armor_table)

# for slot, item in player.weapon.items():
#     if item != None:
#         weapon_table.add_row(f"{slot.title()}, {item.name.title()}, 'ITEM STATS', '3', '20','10'") # {item.stats}
#         for stat, value in item.stats.items():
#             console.print(f"[equipped]{value} [/]",end='')
#             print("")
# print(f"{player.weapon["main-hand"].name}")
# print(f"{player.weapon["main-hand"].sub_class}")
# print(f"{player.weapon}")