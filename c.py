import os, contextlib
from pathlib import Path
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
    console.print(Path.cwd(), style="folder")

    sorted_cwd = sorted(Path.cwd().iterdir(), key=lambda x: x.is_file())
    dir_array = []
    dir_array.append(Path.cwd().parent)
    dir_array.extend(sorted_cwd)

    for i, item in enumerate(dir_array):
        print(i, end="  ")
        if item.is_dir():
            console.print(item.name, style="folder")
        else:
            console.print(item.name)
    return dir_array


def command(dirs):
    """A method to execute commands"""
    command = input("Command: ")
    # If the input begins with a number, assume it's an index and change to that index's directory
    if command[0].isdigit() and int(command) in range(0, len(dirs)):
        try:
        # If the index refers to a folder, change directories:
            if dirs[int(command)].is_dir():
                os.chdir(dirs[int(command)])
        
            if dirs[int(command)].is_file():
                os.startfile(dirs[int(command)])
        except IndexError:
            pass

def app():
    with contextlib.suppress(KeyboardInterrupt):
        while True:
            dir_array = get_files()
            command(dir_array)
        return dir_array[0]

# Executable Code
if __name__ == "__main__":
    last_dir = app()
    print(last_dir)