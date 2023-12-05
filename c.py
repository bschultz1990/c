import pathlib
# import os
# from rich import Console
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import ScrollableContainer


class C(App):
    """A Textual app to display and manage files."""
    CSS_PATH = "styles.css"
    BINDINGS = [
        ("ctrl+c", "quit", "Quit"),
        # ("ctrl+b", "view_basket", "Basket"),
        # ("shift+~", "toggle_terminal", "Terminal"),
        ("ctrl+d", "toggle_dark", "Dark Mode"),
    ]
    ICONS = {
        "file": "\uf4a5",
        "folder": "\uf114",
        "circle_open": "\ueabc",
        "circle_closed": "\uf111",
    }

    def on_mount(self) -> None:
        self.title = FileManager.get_cwd()
        FileManager.get_files(self)

    def action_quit(self) -> None:
        self.exit()

    def compose(self) -> ComposeResult:
        yield Header(classes="main-bg")
        yield ScrollableContainer(classes="main-bg", id="file_container")
        # yield ScrollableContainer(id="basket_container")
        # yield ScrollableContainer(id="terminal_container")
        yield Footer()


class FileManager:
    """A widget to manage the viewing, creating, updating, and deleting of files."""

    def get_files(self) -> None:
        """A method to get files in the current directory."""
        sorted_cwd = sorted(pathlib.Path.cwd().iterdir(),
                            key=lambda x: x.is_file())

        for index, item in enumerate(sorted_cwd):
            file_item = FileItem(f"{index+1} {item.name}")
            file_item.is_selected = False
            file_item.idx = index+1
            file_item.path = item.absolute()
            file_item.itemname = item.name

            if index == 0:
                back = FileItem(f"{index} ..")
                back.idx = index
                back.path = item.parent
                back.itemname = item.name
                back.add_class("folder")
                self.query_one("#file_container").mount(back)

            if item.is_dir():
                file_item.add_class("folder")
            else:
                file_item.add_class("file")

            # file_item.id = (f"{}")
            self.query_one("#file_container").mount(file_item)

    def get_cwd() -> str:
        return pathlib.Path.cwd()


class FileItem(Static):
    """A widget representing individual file items in a directory."""

    def assign(self, idx, path, name):
        self.idx = idx
        self.path = path
        self.itemname = name


if __name__ == "__main__":
    app_instance = C()
    app_instance.run()
