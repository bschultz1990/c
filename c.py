import os, pathlib, contextlib, time
from rich.console import Console
from rich.theme import Theme


theme_default = Theme(
    {
        "index": "bright_black",
        "folder": "deep_sky_blue2",
        "last": "white on cyan",
        "search": "black on green",
    }
)

console = Console(theme=theme_default)

# CONSTANTS


# Functions
def get_files():
    """A method to get files in the current directory"""
    console.clear()
    console.print(pathlib.Path.cwd(), style="folder")

    sorted_cwd = sorted(pathlib.Path.cwd().iterdir(), key=lambda x: x.is_file())
    dir_array = []
    dir_array.append(pathlib.Path.cwd().parent)
    dir_array.extend(sorted_cwd)

    for i, item in enumerate(dir_array):
        print(i, end="  ")
        if item.is_dir():
            console.print(item.name, style="folder")
        else:
            console.print(item.name)


# Executable Code
if __name__ == "__main__":
    get_files()
