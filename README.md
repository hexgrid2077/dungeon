```
██████╗ ██╗   ██╗███╗   ██╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗
██╔══██╗██║   ██║████╗  ██║██╔════╝ ██╔════╝██╔═══██╗████╗  ██║
██║  ██║██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██║   ██║██╔██╗ ██║
██║  ██║██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║   ██║██║╚██╗██║
██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗╚██████╔╝██║ ╚████║
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
```
# Running the game
You will need Rich for the text color and of course Python 3. This is entirely in the terminal.
In the console type:
```shell
pip install -r requirements.txt
```
Once you have that, just run main.py and away you go!

# Dungeon
This project was me learning Object Oriented Programming in Python and having a blast doing it. It reminds me of my friends who played MUDs (Multi User Dungeons) back in the mid 90s and just made my imagination run wild with possibilities.
Who knows, maybe I'll pack it up as a standalone game using NCurses or PyGame, or some browser thing. Doesn't matter, I keep adding and tweaking and my skills have jumped since. If it isn't fun anymore I will stop doing it.

# TODO
**The two bugs here have a similar problem about creating items.**
#FIXME If player has no potions and you get one off of an enemy in battle, it doesn't have the setup_weapon_armor_consumable_object function in the Battle class.'
It is already in battle_class in line 37-38. Must recreate the bug.
# Loot menu
#FIXME picking up individual items has some mission arguments.
# Current Mission
- Looks like my repo is setup as mikeherb or hexgrid2077 in github but my personal repo name on my thinkpad is mikeherb. I don't know. 
- Scan Area still has white font lol
- if we dump to json files on the inventory thing, can we edit items monsters and locations in excel?
## Battle System
- The shield doesn't have any defense stats
## player_attack_roll
- the combatants, turn order which could depend on speed, runs the loop til one dies or flees, victory /defeat cleanup to trigger the loot process.
- Player death. Once we have player death and maybe a boss, the game is complete and then we are in improvements.
- test battle with gear on vs wraith
- Get the player attack roll function working and do the same for the enemy.
- Show the enemy status like "Healthy, limping a bit, almost dead"
- show the death blow
- speed as a factor like... a list of who goes turn by turn based on speed. or a **roll** between each turn to see who goes first. So fast enemies could throttle you.
- Make enemy loot drops a random selection of a few items.
- flesh out 2 other enemies quick for some variety
- Do I want a battle prompt to flee or leave it?
- physical weaknesses for monsters.
- Add attack type to weapons (slashing, impact, piercing)

# Experience
- Each area is a curated experience like a D&D package you'd buy at Sentry Box, with a grand boss, some lore, keys and quest items, traps etc.
- Treasure chests instead of just laying on the floor. You can open the treasure chest and then the contents are available to take.
- Quest items like lost letters you can read and get clues/lore
- keys that can open doors in sub menus, or open chests.
- props as objects that would include chests, doors, levers with their own sub menus
## FIXES

- if the player only has one item of that armor/weapon sub_class, just equip it, don't make them push 1. You would have to tally up all items and see how many are in each subclass.
# Engine
## Display

- we will be using Rich **Layouts** when the game mechanic basics are running.
	- https://rich.readthedocs.io/en/stable/layout.html
	- https://github.com/Textualize/rich/blob/master/examples/fullscreen.py
## Inventory & Equipment
### Inventory System
- If the weapon or armor is better than what you have in that slot, have a green up-arrow or red down-arrow.
- Convert the item_master.py to a json file you can edit in excel.
#### Submenu refactor
- use "args" in a function for the case choices in the inventory_menu_class.
- Build a submenu class that you can insert a dictionary like a: Armor, w: weapons and it would prompt the user with the standard menu and go from the optoins to the function. 
- Refactor submenus using menu.get(choice) like in `engine.py`
- Fix nested match bullshit in the inventory page to be a reusable function

# Classes
### Player Class functions to do
- methods:  use(), handin(), *sneak(), inventory(), drop(), buy(), sell(), view()
### Enemy Class
- methods: attack description
### Item Class
- Name, description, price (*quest item won't inherit price*)
#### Quest Item Subclass
- plot importance
- hand-in flag
- Can't be sold or dropped
- Keys that unlock new areas! Like a Metroidvania type thing.
### Shop
- Have a shop to buy new gear and sell their junk.
## Battles
- Enemies have very random loot. Right now the wraith drops a potion and 25 gold every fight.
- manual attack item run options so you can get away or heal if you need.
- Very much like the original Ultima games to start. Maybe a party later with companions you could encounter or hire at the tavern.
- Enemies can blend in with the current surroundings like... Skeleton does a backflip off the stairs.
- Shows items found in a cool way plus their stats
- Mimic something like Demonlord to start
- speed toggle (fast medium slow) between lines.
### Classes
- https://tutorialsflood.com/python-text-based-rpg-game-user-input-and-exploration-56dd3454a74f

# Environment
## NPCs
- Vampire barkeep that runs the tavern and gives you quests, like the one in Symphony of the Night. 
	- This is where you respawn after you die and lose your gold or something. Or maybe your weapon durability drops to half or you lost all your inventory except a sword or... permanent death.
- Crusader wandering the halls that you can randomly run into and then he gives you a sidequest, to meet at the graveyard for a special sigil that gives you +9 to all skills.
- Lost hunter dying that you have to mercy kill or have a choice which affects something later in the game.
- Have a spot at the fountain of life where the player can refill life if the potions get scarce. Like a home base while they're working through the dungeon.

## Maps
- Add a legend to tell where the player is, and where the exit is.
- can interlock different map areas with the exits. A warp stone or something can transport you back to the tavern.
- Maps and locations on separate files, eventually into a JSON file so we don't have a massive file.
- Inventory would be stored in a JSON file for each room so that when you pick an item up, it's gone from the map.
- Down the road add up/down options like a 3D grid?
- Story section that is separate from the environment ie - you wake up in the darkness, what is this place? And then you get up. .. description: you're in a crypt.
- **ZONES** so you have a forest zone with a map, a dungeon zone with multiple floors, a tavern zone. When you switch zones it would load a new json file
### Map Menu
- Check if left right up or down exists or is a wall and then show the symbols on a little 3x3 map.
### Map Editor
- Customtkinter grid of square icons with the coordinate tuple (1,2) that you could click on and then have an up down left right option to CREATE if it doesn't exist or MOVE to... And each one would bring up the dictionary/json fields like name, coordinate, description, enemies, enemy odds with a save option.
- You could create new areas like this really easily.
- Also have a monster, item and equipment editor.
- Map editor that would edit a JSON file.
- Would be better than excel because you get a map too.
- CustomTkinter frame with a centered Map.
- [[Tkinter]] or [[pyqt]] interface that you could add items from the item database to... Or edit the item database in Excel
## Quest Log
- Simple quest like defeat so and so at (3,3)
- Other options like look, pick lock
# Menu
## Saving/Loading
- New Game or Save and load to a JSON file or text file? Current location, inventory list, locations too because they hold the data for inventory on the ground
- Ascii title
- SICK Ascii art with a save/load function
- there are only objects in the player inventory and we can offload those into a dictionary and have a routine that uses the starting inventory list to build objects out of them too.
# Ongoing Polish
- setup error protection with exceptions to idiot proof it.
- If we keep going with this, GUI client with a map and some other inventory button stuff.
- Use [[rich]] textwrap and maybe pick a terminal column width
- Refactoring the inventory page into the player class as we go. Watch out for circular imports so test after every migration.
# Down the road ideas
- Fire up Realms of Despair and make an account.
- Play the old Ultima, Wizardry and Demonlord games.
- A wolf or a battle cat friend that helps you search items or gives you rides
- Have the rich function that highlights or bolds keywords, basically anything in the monster or item dictionaries.
- player gets ability to see monsters hp mp and weaknesses, maybe resistances  Skill tree like weapon mastery or something.
- [[list Comprehension]] to do some of the rolodex running on that equipment section.
- piercing ignores some armor, slashes have bleeding effects, blunt damage could stun them
- Tkinter map editor to add items from the database, monsters, descriptions and save them to the json file.
- tkinter item and monster editor That saves them to a json file.
- Items have weight
- Areas where you can climb a rope, fall through a trap door
- pygcurse? https://github.com/asweigart/pygcurse