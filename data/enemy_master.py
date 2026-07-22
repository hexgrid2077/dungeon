# Skeleton Warrior
# Skeleton Mage
# Walking corpse

enemy_master = {
    "wraith":{
        "source":"enemy_master",
        "species":"undead",
        "description":"an aparition who makes the surrounding air freeze",
        "hp":60,
        "mp":10,
        "stats":{
            "atk":35, # FIXME was 35 but trying to kill the player
            "def":25,
            "dex":10,
            "int":10,
            "crit":10,
            },
        "actions":["slashes at you","tackles you","curses you with its death gaze", "takes a spinning swipe at you"],
        "taunt":"Welcome to the netherworld, mortal!",
        "loot":{
            "gold":20,
            "health potion":1,
            },
        },
 }