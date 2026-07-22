import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.treasure = 0

    def is_alive(self):
        return self.health > 0
    
    def print_status(self):
        print(f"{self.name}: Health = {self.health}, Attack = {self.attack}, Defense = {self.defense}, Treasure = {self.treasure}")


class Enemy:
    def __init__(self, name, health, attack, defense, golden_reward):
        self.name = name
        self.health = health
        self.attacking = attack
        self.defense = defense
        self.golden_reward = golden_reward

    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage

    def print_status(self):
        print(f"{self.name}: Health = {self.health}, Attacking = {self.attacking}, Defense = {self.defense}")


def battle(player, enemy):
    print("A fierce", enemy.name, "attacks!")
    while player.is_alive() and enemy.is_alive():
        print("\n" + "-" * 20)
        player.print_status()
        enemy.print_status()
        print("-" * 20 + "\n")

        player_damage = max(0, player.attack - enemy.defense)
        enemy.take_damage(player_damage)
        print(f"You hit the {enemy.name} for {player_damage} damage")

        if enemy.is_alive():
            enemy_damage = max(0, enemy.attacking - player.defense)
            player.health -= enemy_damage
            print(f"The {enemy.name} strikes you for {enemy_damage} damage.")

    if player.is_alive():
        print("\nVictory! You have defeated the", enemy.name + "!")
        player.treasure += enemy.golden_reward
        print(f"You loot {enemy.golden_reward} gold from the {enemy.name}.")
    else:
        print("\nYou have been slain by the", enemy.name + "!")
        print("Game Over")

player_name = input("Enter your name: ")
player = Player(player_name)

enemy1 = Enemy("Orc", 30, 8, 2, 10)
enemy2 = Enemy("Giant Spider", 40, 12, 4, 15)
enemy3 = Enemy("Sorcerer", 50, 15, 5, 20)

enemies = [enemy1, enemy2, enemy3]

print("\nWelcome to the Fantasy Adventure RPG!\n")

while player.is_alive():
    enemy = random.choice(enemies)
    battle(player, enemy)
    if not input("Do you want to play another game? (yes/no): ").lower().startswith("y"):
        break