import time

from rich.live import Live
from rich.table import Table

items = ["apples", "sink", "banana", "Peanutbutter", "dishwasher", "magicbullet", "glass"]

with Live(refresh_per_second=4) as live:  # update 4 times a second to feel fluid
    # for row in range(12):
    #    live.console.print(f"Working on row #{row}")
    #    time.sleep(0.4)
        # table.add_row(f"{row}", f"description {row}", "[red]ERROR")
    for item in items:
        print(item)
        time.sleep(0.4)
