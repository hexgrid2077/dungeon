from data.maps.crypt import locations
from rich.console import Console
from data.data_files.config import hud_theme
console = Console(theme=hud_theme, highlight=False)

class Game_Map:
    def __init__(self, locations, current_location, exit_location):
        self.locations = locations
        self.current_location = current_location
        self.exit_location = exit_location
        self.show_map()

    def get_totals(self):
        columnlist = []
        rowlist = []
        coordlist = []
        for key, value in self.locations.items():
            columnlist.append(key[0])
            rowlist.append(key[1])
        columnlist = list(set(columnlist))
        rowlist = list(set(rowlist))
        for key in locations.keys():
            coordlist.append(key)
        return rowlist, columnlist, coordlist

    def show_map(self):
        rowlist, columnlist, coordlist = self.get_totals()
        # Print Top Wall
        console.print("")
        console.print("\t\t#", end="", style="map_wall") # Left border
        for column in range(len(columnlist)+3):
            console.print("##",end="", style="map_wall")
        console.print("##", style="map_wall") # Right border

        # Print Map
        for y in range(max(rowlist), min(rowlist)-1, -1):
            console.print("\t\t##", end="", style="map_wall")
            for x in range(len(columnlist)):
                coord_check = (x,y)
                if coord_check in coordlist:   # If the tuple equals a tuple in the coordlist, print " . ". if not, SPACE
                    if coord_check == self.current_location:
                        console.print(" @ ", end="", style="map_player")
                    elif coord_check == self.exit_location:
                        console.print(" X ", end="", style="map_exit")    
                    else:
                        console.print(" - ", end="", style="map_location")
                elif coord_check not in coordlist:
                    console.print("###", end="", style="map_wall")
            console.print("##",end="", style="map_wall")
            console.print("")

        # Print Bottom Wall
        console.print("\t\t#", end="", style="map_wall") # Left border
        for column in range(len(columnlist)+3):
            console.print("##",end="", style="map_wall")
        console.print("##",end="", style="map_wall") # Right border
        console.print("\n\n")

# TODO CHALLENGE: maybe only add a fog of war like coordinates you can see so walls or rooms in visible exits.

# game_map = Game_Map(locations, (1,1))