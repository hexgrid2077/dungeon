from rich import print
from rich.layout import Layout
from rich.panel import Panel

layout = Layout()

layout.split_column(
    Layout(name="upper"),
    Layout(name="lower"),
)

layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right")
)

layout["right"].split(
    Layout(Panel("Hello")),
    Layout(Panel("World"))
)

layout["left"].update(
    "The mystery of life isn't a problem to solve, but a reality to experience."
)

layout["upper"].visible = True
print(layout.tree)