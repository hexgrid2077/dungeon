from data.enemy_master import enemy_master


class Enemy:
    def __init__(self, name, species, description, hp, mp, stats, actions, taunt, loot):
        self.name = name
        self.species = species
        self.description = description
        self.hp = hp
        self.mp = mp
        self.stats = stats
        self.actions = actions
        self.taunt = taunt
        self.loot = loot
    
    def is_alive(self):
        if self.hp > 0:
            return True
        
    def attack(self):
        ...


def create_enemy(name):
    name = Enemy(
        name, # This is the name
        enemy_master[name]["species"],
        enemy_master[name]["description"],
        enemy_master[name]["hp"],
        enemy_master[name]["mp"],
        enemy_master[name]["stats"],
        enemy_master[name]["actions"],
        enemy_master[name]["taunt"],
        enemy_master[name]["loot"],)
    return name
        # Need this, obv
        

# Inherit here and make some enemies.