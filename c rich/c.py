import os, pathlib, contextlib, time
from rich.console import Console
from rich.theme import Theme


theme_default = Theme(
    {
        "default": "white",
        "index": "bright_black",
        "folder": "deep_sky_blue2",
        "last": "white on cyan",
        "search": "black on green",
    }
)

console = Console(theme=theme_default)

# CONSTANTS


# Functions


def header():
    """A method to print the header, including current directory."""
    console.print(pathlib.Path.cwd(), style="folder")


def get_files():
    """A method to get files in the current directory"""
    sorted_cwd = sorted(pathlib.Path.cwd().iterdir(), key=lambda x: x.is_file())
    for index, item in enumerate(sorted_cwd):
        console.print(f"{index}. {item.name}")


# Executable Code
if __name__ == "__main__":
    console.clear()
    header()
    get_files()
