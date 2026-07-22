from rich.console import Console
from rich.table import Table
from data.data_files.config import hud_theme

console = Console(theme=hud_theme, highlight=False)

weapon_temp = []
armor_temp = []
cons_temp = []
quest_temp = []
list_of_temps = [weapon_temp, armor_temp, cons_temp, quest_temp]

def item_class_sorter(player):
    # Start with a fresh list
    for temp in list_of_temps:
        temp.clear()
    for key, value in player.rucksack.items():
        match value.item_class:
            case "Weapon":
                weapon_temp.append((key,value.qty))
            case "Armor":
                armor_temp.append((key,value.qty))
            case "Consumable":
                if value.name != "gold":
                    cons_temp.append((key,value.qty))
            case "Quest":
                quest_temp.append((key,value.qty))


def list_items():       
    if weapon_temp: console.print("\nWeapons", style="weapons", justify="left")
    for item in weapon_temp:
        console.print(f"{item[0].title()} x {item[1]}")
    if armor_temp: console.print("\nArmor", style="armor")
    for item in armor_temp:
        console.print(f"{item[0].title()} x {item[1]}")
    if cons_temp: console.print("\nConsumables", style="consumable")
    for item in cons_temp:
        console.print(f"{item[0].title()} x {item[1]}")
    if quest_temp: console.print("\nQuest Items", style="quest")
    for item in quest_temp:
        console.print(f"{item[0].title()} x {item[1]}")


def print_equipped_items(player):
    console.print("\nEquipment", style="submenu")
    weapon_table = Table(title="[weapons]Weapons[/]", box=None, show_header=True, show_footer=False, padding=0, title_justify="left")
    weapon_table.add_column("[weapons]Slot", width=15)
    weapon_table.add_column("[weapons]Item", width=20)
    weapon_table.add_column("[weapons]Attack", width=12, justify="center")
    weapon_table.add_column("[weapons]Dexterity", width=12, justify="center")
    weapon_table.add_column("[weapons]Critical", width=12, justify="center")

    for slot, item in player.weapon.items():
        if item != None:
            weapon_table.add_row(f"[grayed]{slot.title()}[/]", f"{item.name.title()}", f"{item.stats["atk"]}",\
                                        f"{item.stats["dex"]}", f"{item.stats["crit"]}")
        else:
            weapon_table.add_row(f"[grayed]{slot.title()}[/]", f"[grayed]Not Equipped[/]")


    armor_table = Table(title="[armor]Armor[/]", box=None, show_header=True, show_footer=False, padding=0, title_justify="left")
    armor_table.add_column("[armor]Slot", width=15)
    armor_table.add_column("[armor]Item", width=20)
    armor_table.add_column("[armor]Defense", width=12, justify="center")
    armor_table.add_column("[armor]Dexterity", width=12, justify="center")
    armor_table.add_column("[armor]Resistance", width=12, justify="center")

    for slot, item in player.armor.items():
        if item != None:
            armor_table.add_row(f"[grayed]{slot.title()}[/]", f"{item.name.title()}", f"{item.stats["def"]}",\
                                        f"{item.stats["dex"]}", f"{item.stats["resist"]}")
        else:
            armor_table.add_row(f"[grayed]{slot.title()}[/]", f"[grayed]Not Equipped[/]")

    print("")
    console.print(weapon_table)
    print("")
    console.print(armor_table)

    console.print("\n[b u]W[/]eapons | [b u]A[/]rmor | [b u]B[/]ack", style="submenu")
    console.print("> ", style="prompt",end='')
    
    eq_weap_armr_choice = input("").lower()


    def match_eq_weap_armr_choice(player):
        match eq_weap_armr_choice:
            case "w":
                equip_weapon_submenu(player)
            case "a":
                equip_armor_submenu(player)
            case "b":
                show_inventory(player)


    def equip_weapon_submenu(player):
        item_class_sorter(player)
        mainhand_temp_list = []
        offhand_temp_list = []

        # Sort into each sub_class
        for key, value in player.rucksack.items():
            if value.sub_class == "main-hand":
                mainhand_temp_list.append(key)
            elif value.sub_class == "off-hand":
                offhand_temp_list.append(key) 

        # Main-Hand list
        console.print(f"\nMain-Hand:", style="submenu")
        numerated_list = list(enumerate(mainhand_temp_list))
        for option in numerated_list:
            console.print(f"{option[1].title()}")

        # Off-Hand list
        console.print(f"\nOff-Hand:", style="submenu")
        numerated_list = list(enumerate(offhand_temp_list))
        for option in numerated_list:
            console.print(f"{option[1].title()}")

        console.print("\n[b u]M[/]ain-Hand | [b u]O[/]ff-Hand", style="submenu")
        console.print("> ", style="prompt", end='')
        mainhand_offhand = input("").lower()

        def mainhand_submenu(player):
            player.transfer_to_equipped("main-hand", "weapon")

        def offhand_submenu(player):
            player.transfer_to_equipped("off-hand", "weapon")

        def match_mainhand_offhand(player):
            match mainhand_offhand:
                case "m":
                    mainhand_submenu(player)
                case "o":
                    offhand_submenu(player)
        
        match_mainhand_offhand(player)


    def equip_armor_submenu(player):
        item_class_sorter(player)
        head_temp_list = []
        body_temp_list = []
        hands_temp_list = []
        feet_temp_list = []

        # Sort into each sub_class
        for key, value in player.rucksack.items():
            if value.sub_class == "head":
                head_temp_list.append(key)
            elif value.sub_class == "body":
                body_temp_list.append(key)
            elif value.sub_class == "hands":
                hands_temp_list.append(key)     
            elif value.sub_class == "feet":
                feet_temp_list.append(key)     

        # Head list
        console.print(f"\n[b u]H[/]ead:", style="submenu")
        numerated_list = list(enumerate(head_temp_list))
        for option in numerated_list:
            console.print(f"{option[1].title()}")

        # Body list
        console.print(f"\n[b u]B[/]ody:", style="submenu")
        numerated_list = list(enumerate(body_temp_list))
        for option in numerated_list:
            console.print(f"{option[1].title()}")

        # Hands list
        console.print(f"\nH[b u]a[/]nds:", style="submenu")
        numerated_list = list(enumerate(hands_temp_list))
        for option in numerated_list:
            console.print(f"{option[1].title()}")

        # Feet list
        console.print(f"\n[b u]F[/]eet:", style="submenu")
        numerated_list = list(enumerate(feet_temp_list))
        for option in numerated_list:
            console.print(f"{option[1].title()}")

        if head_temp_list or body_temp_list or hands_temp_list or feet_temp_list:
            console.print("\n[b u]H[/]ead | [b u]B[/]ody | H[b u]a[/]nds | [b u]F[/]eet", style="submenu")
            console.print("> ", style="prompt", end='')
            head_body_hands_feet = input("").lower()
        else:
            console.print("\nNO ARMOR ITEMS TO EQUIP. PRESS ENTER TO CONTINUE", style="submenu")
            console.print("> ", style="prompt", end='')
            head_body_hands_feet = input("").lower()

        def head_submenu(player):
            player.transfer_to_equipped("head", "armor")

        def body_submenu(player):
            player.transfer_to_equipped("body", "armor")

        def hands_submenu(player):
            player.transfer_to_equipped("hands", "armor")

        def feet_submenu(player):
            player.transfer_to_equipped("feet", "armor")

        def match_head_body_hands_feet(player):
            match head_body_hands_feet:
                case "h":
                    head_submenu(player)
                case "b":
                    body_submenu(player)
                case "a":
                    hands_submenu(player)
                case "f":
                    feet_submenu(player)

        match_head_body_hands_feet(player)


    match_eq_weap_armr_choice(player)

# TODO Start here for the refactor.
def show_inventory(player):
    item_class_sorter(player)
    list_items()

    console.print("\n[b u]E[/]quip Weapons & Armor | [b u]U[/]se Items | [b u]Q[/]uest Items | [b u]B[/]ack", style="submenu")
    console.print("> ", style="prompt",end='')
    submenu_choice = input("").lower()


    def match_submenu(submenu_choice, player):
        match submenu_choice:
            case "e":
                print_equipped_items(player)
            case "u":
                consumable_submenu(player)
            case "q":
                quest_submenu()
            case "b":
                pass
            case _:
                show_inventory(player)

    def quest_submenu():
        console.print("quest items")

    match_submenu(submenu_choice, player)

def consumable_submenu(player):

    console.print(f"\nItem Options:", style="submenu")
    numerated_list = list(enumerate(cons_temp))
    for option in numerated_list:
        print(f"{option[0]+1}) {option[1][0].title()} x {option[1][1]}")
    console.print("\nChoose Number:")
    console.print("> ", style="prompt", end='')
    consume_choice = int(input(""))
    consume_choice -= 1 # Shift back to starting at 0.
    try:
        chosen_item_name = cons_temp[consume_choice][0]
        print(f"Going to consume {chosen_item_name.title()}")
        player.use_item(chosen_item_name)

    except IndexError:
        print("You do not have this item.")
        consumable_submenu(player)
        # FIXME This needs a back option if you don't want to use anything.







