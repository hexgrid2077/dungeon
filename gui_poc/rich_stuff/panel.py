import rich
from rich.console import Console
from rich.status import Status
from rich.panel import Panel
Panel.fit("[bold yellow]Hi, I'm a Panel", border_style="red")

console = Console()
status = Status()
console.rule("[bold red]Chapter 2")

with console.status("Working..."):
    do_work()
