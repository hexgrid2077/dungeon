from rich import print
from rich.layout import Layout
from rich.panel import Panel
import time
from rich.console import Console

layout = Layout()
console = Console()

layout.split_column(
    Layout(name="upper", size=10),
    Layout(name="lower")
)

layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
)

layout["right"].split(
    Layout(Panel("Hello")),
    Layout(Panel("World!")),
)

items = ["apples", "sink", "banana", "Peanutbutter", "dishwasher", "magicbullet", "glass"]
fuddruckers = """
    [red]fuddruckers[/]
    is
    Hello
    best
    """

layout["left"].update(
    "Testing this again.",
)
print(layout)
time.sleep(1)

layout["left"].update(
    fuddruckers, 
    #console.input("input>>")
)
print(layout)

