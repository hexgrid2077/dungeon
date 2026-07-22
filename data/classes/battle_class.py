from random import randint, choice
from time import sleep
from rich.console import Console
from data.data_files.config import hud_theme
from data.classes.item_class import Item
from data.data_files import signs

console = Console(theme=hud_theme, highlight=False)

class Battle:
    def __init__(self, enemy, player):
        self.enemy = enemy
        self.player = player

    def player_actions(self,player):
        if player.weapon["main-hand"] != None:
            #TODO add weapon verbs here.
            attack_verbs = ["slash","swipe","stab","smash"]
            return choice(attack_verbs)
        else:
            unarmed_verbs = ["tackle","throw a haymaker at","elbow","roundhouse kick"]
            return choice(unarmed_verbs)


    def loot_corpse(self, player, enemy):
        console.print(f"\n\t\t[b]YOU KILLED THE {enemy.name.upper()}!", style="menu")
        console.print(f"\nThe [enemy]{enemy.name.title()}[/] dropped:")
        for item, qty in enemy.loot.items():
            console.print(f"[loot]{item.title()}[/] x {qty}")
        self.create_loot_objects(player, enemy)
        return False


    def create_loot_objects(self, player, enemy):
        for item, qty in enemy.loot.items():
            if item in player.rucksack:
                player.rucksack[item].qty += qty
            else:
                player.rucksack[item] = Item.create_item(self, item)      

    def player_attack_roll(self, player, enemy):
        print(f"Player Stats: {player.stats}")
        print(f"Enemy Stats: {enemy.stats}")
        print("")

        # Chance to dodge
        player_dodge = float(player.stats["dex"]/100)
        print(f"Player dodge: {player_dodge}")
        enemy_dodge = float(enemy.stats["dex"]/100)
        print(f"Enemy dodge: {enemy_dodge}")


        print("")
        # Chance to hit Critical
        player_crit_chance = float(player.stats["crit"]/100)
        print(f"player_crit_chance {player_crit_chance}")
        enemy_crit_chance = float(enemy.stats["crit"]/100)
        print(f"Enemy_crit_chance {enemy_crit_chance}")

        print("")

        # Player attack damage (player atk - enemy def)
        player_atk = player.stats["atk"] - enemy.stats["def"]
        r1 = randint((round(player_atk/2)),(round(player_atk)))
        r2 = randint((round(player_atk/2)),(round(player_atk)))
        player_atk = r1+r2
        print(f"Player Attack:\t{player_atk}")

        
        # Enemy attack damage (enemy atk - player def)
        enemy_atk = enemy.stats["atk"] - player.stats["def"]
        r1 = randint((round(enemy_atk/2)),(round(enemy_atk)))
        r2 = randint((round(enemy_atk/2)),(round(enemy_atk)))
        enemy_atk = r1+r2
        print(f"Enemy Attack:\t{enemy_atk}")


    def loop(self, player, enemy):
        console.print(signs.battle_title, style="weapons")
        # console.print("------------------------------- BATTLE -----------------------------", style="enemy")
        console.print(f"\nYou encounter a [enemy]{enemy.name.title()}[/], {enemy.description}...")
        console.print(f"[taunt]\"{enemy.taunt}\"[/]\n")
        sleep(1)

        while player.is_alive() and enemy.is_alive():
            if player.weapon["main-hand"].name:
                weapon = player.weapon["main-hand"].name
            console.print("--------------------------------------------------------------------", style="exit")
            console.print(f"HP {player.hp}/{player.max_hp}")

            player_attack_damage = randint(0,player.stats["atk"])
            enemy_attack_damage = randint(0,enemy.stats["atk"])

            if player_attack_damage == 0:
                console.print(f"You [weapons]{self.player_actions(player)}[/] the [enemy]{enemy.name.title()}[/] with your [weapons]{weapon.title()}[/] and [attacked]miss![/]")
            else:
                console.print(f"You [weapons]{self.player_actions(player)}[/] the [enemy]{enemy.name.title()}[/] with your [weapons]{weapon.title()}[/] for {player_attack_damage} damage!")

            enemy.hp -= player_attack_damage

            if not enemy.is_alive():

                self.loot_corpse(player, enemy)
            else:
                console.print(f"The [enemy]{enemy.name.title()}[/] [attacked]{choice(enemy.actions)}[/] doing {enemy_attack_damage} damage!")
                player.hp -= enemy_attack_damage
                sleep(1)
