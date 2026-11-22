"""Everything built with rich."""
from rich import box
from rich.console import Console
from rich.markup import escape
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.table import Table

console = Console()


def banner():
    console.print(Panel.fit("[bold cyan]ONLINE QUIZ[/bold cyan]\n[dim]Python Final Project - Group C[/dim]",
                            border_style="cyan", box=box.DOUBLE, padding=(1, 6)))


def success(msg):
    console.print(f"[bold green]Success:[/bold green] {escape(msg)}")


def warning(msg):
    console.print(f"[yellow]Warning:[/yellow] {escape(msg)}")


def error(msg):
    console.print(f"[bold red]Error:[/bold red] {escape(msg)}")


def show_table(title, columns, rows):
    table = Table(title=title, box=box.ROUNDED, header_style="bold magenta")
    for column in columns:
        table.add_column(column)
    for row in rows:
        table.add_row(*[escape(str(cell)) for cell in row])
    console.print(table)


def show_menu():
    console.print(Panel(
        "1. Show questions\n2. Add question\n3. Load from internet\n"
        "4. Start quiz\n5. Leaderboard\n6. Player statistics\n7. Chart\n8. Exit",
        title="Menu", border_style="cyan", box=box.ROUNDED))
    return Prompt.ask("Choice", choices=[str(i) for i in range(1, 9)])


def login():
    for _ in range(3):
        user = Prompt.ask("Username")
        password = Prompt.ask("Password", password=True)
        if user == "admin" and password == "Py@12345":
            return True
        error("Wrong username or password.")
    return False


def ask_text(label):
    return Prompt.ask(label).strip()


def ask_int(label):
    return IntPrompt.ask(label)


def ask_choice(label, choices):
    return Prompt.ask(label, choices=choices)


def ask_question(number, total, question):
    console.rule(f"Question {number}/{total}  ({question.points()} pt)")
    console.print(escape(question.display()))
    return Prompt.ask("Your answer", choices=question.choices())
