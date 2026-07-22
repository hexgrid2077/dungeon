'''
--- TO ADD ---

 '''

consumable_master = {
    "gold":{
        "source":"consumable_master",
        "item_class":"Consumable",
        "sub_class":"currency",
        "description":"A shiny gold coin. Arrr!",
        "stats":{
            "hp":0,
            "mp":0,
            "status":"",
                },
        "price":1,
        },

    "health potion":{
        "source":"consumable_master",
        "item_class":"Consumable",
        "sub_class":"potion",
        "description":"A potion of healing",
        "stats":{
            "hp":30,
            "mp":0,
            "status":"",
                },
        "price":50,
        },

    "water skin":{
        "source":"consumable_master",
        "item_class":"Consumable",
        "sub_class":"food",
        "description":"A leather skin with springwater",
        "stats":{
            "hp":50,
            "mp":0,
            "status":"",
                },
        "price":30,
        },
    
}

weapon_master = {
    "buckler shield":{
        "source":"weapon_master",
        "item_class": "Weapon",
        "sub_class":"off-hand",
        "description":"A small shield carved from the finest particle board.",
        "stats":{
            "atk":0,
            "dex":0,
            "crit":2,
                },
        "price":50,
        },

    "rusty dagger":{
        "source":"weapon_master",
        "item_class": "Weapon",
        "sub_class":"main-hand",
        "description":"May require a tetanus shot. Adds +9 against Ogres.",
        "stats":{
            "atk":25,
            "dex":10,
            "crit":10,
                },
        "price":50,
        },

    "torch":{
        "source":"weapon_master",
        "item_class": "Weapon",
        "sub_class":"off-hand",
        "description":"These existed before your cellphone flashlight.",
        "stats":{
            "atk":1,
            "dex":1,
            "crit":0,
                },
        "price":5,
        },
        
    "woodsman axe":{
        "source":"weapon_master",
        "item_class": "Weapon",
        "sub_class":"main-hand",
        "description":"For those cozy camping weekends.",
        "stats":{
            "atk":30,
            "dex":3,
            "crit":5,
                },
        "price":50,
        },
}

armor_master = {
    "cloth tunic":
        {
        "source":"armor_master",
        "item_class": "Armor",
        "sub_class":"body",
        "description":"Cheap tunic of the peasants.",
        "stats":{
            "def":10,
            "dex":0,
            "resist":"-",
                },
        "price":5,
        },

    "leather boots":
        {
        "source":"armor_master",
        "item_class": "Armor",
        "sub_class":"feet",
        "description":"Worst boots evar!",
        "stats":{
            "def":5,
            "dex":2,
            "resist":"-",
                },
        "price":5,
        },

    "leather gloves":
        {
        "source":"armor_master",
        "item_class": "Armor",
        "sub_class":"hands",
        "description":"Keep your digits warm in these troubling times.",
        "stats":{
            "def":5,
            "dex":2,
            "resist":"-",
                },
        "price":5,
        },

    "crusader helmet":
        {
        "source":"armor_master",
        "item_class": "Armor",
        "sub_class":"head",
        "description":"Looks pretty dope for first level gear.",
        "stats":{
            "def":5,
            "dex":0,
            "resist":"-",
                },
        "price":5,
        },
}

quest_master = {
    "graveyard sigil":{
        "source":"quest_master",
        "item_class": "Quest",
        "sub_class":"key",
        "description":"Shaped like an ankh. Maybe it opens a secret door...",
        "quest":"aesop's fable",
        },

}


starting_items = [
    ("gold", 25),
    ("torch", 2),
    ("graveyard sigil", 1),
    ("health potion", 2),
    ("rusty dagger", 1),
    ("water skin", 1),

    ]

starting_equipment = [    # Can only have one of each item here.
    ("woodsman axe", 1),
    # ("buckler shield", 1),
    ("cloth tunic", 1),
    ("leather boots", 1),
    ("leather gloves", 1),
    ("crusader helmet", 1),
    ]