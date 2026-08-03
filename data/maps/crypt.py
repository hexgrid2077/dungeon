exit_location = (2,-1)
locations = {
    # Crypt - Starting place
    (0,0):{
        "name":"crypt",
        "description":"You wake up in the darkness with a scorching pain in your jaw...\nYou realize you're in an underground crypt.\n"
        "There is light coming in from the staircase to the [bold]north[/].\n"
        "A fallen [enemy]skeleton warrior[/] lays with bones scattered everywhere...\n",
        "items":{
            "rusty dagger":2,
            "cloth tunic":1,
            "buckler shield":1,
            "gold":50,
            },
        "enemies":{
            (0,100):"clear",
            },
        "visited":"n",
        },

    # Stone Staircase
    (0,1):{
        "name":"stone staircase",
        "description":"You're on a massive chipped stone staircase that feels thousands of years old.",
        "items":{
            "torch":1,
            },
        "enemies":{
            (0,30):"wraith",
            (31,100):"clear",
            },
        "visited":"n",
        },
   
    # Fountain of Life
    (0,2):{
        "name":"fountain of life",
        "description":"In its own secluded stone area is a fountain beaming with energy.",
        "items":{
            "water skin":1,
            },
        "enemies":{
            (0,30):"wraith",
            (31,100):"clear",
            },
        "visited":"n",
        },

    # Pit of Snakes
    (1,0):{
        "name":"pit of snakes",
        "description":"There is a large pit from broken stones that goes into a deep chasm. You peek down and see dozens of snakes, hissing and "
        "crawling overtop each other.",
        "items":{
            "cloth tunic":1,
            },
        "enemies":{
            (0,30):"wraith",
            (31,100):"clear",
            },
        "visited":"n",
        },

    # Haunted Woods
    (1,1):{
        "name":"haunted woods",
        "description":"You wander outside of the castle into the Haunted Woods",
        "items":{
            
            },
        "enemies":{
            (0,30):"wraith",
            (31,100):"clear",
            },
        "visited":"n",
        },

    # Bridge
    (2,0):{
        "name":"bridge",
        "description":"Placeholder",
        "items":{
            
            },
        "enemies":{
            (0,1):"wraith",
            (2,100):"clear",
            },
        "visited":"n",
        },

    # STAIRS
    (2,-1):{
        "name":"stairs to town",
        "description":"A staircase to get out of the dungeon",
        "items":{
            
            },
        "enemies":{
            (0,1):"wraith",
            (2,100):"clear",
            },
        "visited":"n",
        },

    # Tunnel
    (3,0):{
        "name":"Tunnel",
        "description":"A tunnel past the bridge",
        "items":{
            
            },
        "enemies":{
            (0,1):"wraith",
            (2,100):"clear",
            },
        "visited":"n",
        },

    # Black well
    (4,0):{
        "name":"Black Well",
        "description":"A well that looks into the darkness",
        "items":{
            
            },
        "enemies":{
            (0,1):"wraith",
            (2,100):"clear",
            },
        "visited":"n",
        },

    # Torture Chamber
    (4,1):{
        "name":"Torture Chamber",
        "description":"the Cat o-nine-tails",
        "items":{
            
            },
        "enemies":{
            (0,1):"wraith",
            (2,100):"clear",
            },
        "visited":"n",
        },
}



