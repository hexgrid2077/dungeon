from random import choice

random_dialog = [
    # "[italic #FD8C00]Max the cat is pawing at the corpse, and judging you. He would like a belly rub and some treats.[/]",
    "[italic #837099]Vladimir: It's about time somebody went down there and figured out what the hell was going on.[/]",
    "[italic #837099]The vampire barkeep pours himself a blood mai tai up in the tavern.[/]",
    "[italic #837099]Vladimir: Hey meatbag, stop by the tavern later. I have a rat problem...[/]",
    "[italic #837099]Vladimir: You're supposed to stab them with the pointy end, mortal![/]",
    "[italic #837099]Vladimir: Make sure you bring me back something that isn't junk, mortal.[/]",
]

def say_something_random():
    return choice(random_dialog)

