####################################################################################################
# This file serves as the starting point for the application.
# How to run the application: `python -m ivc`
####################################################################################################

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from src import Chatbot


class IVCApp(App):

    """A Textual application to serve the IVC (Intelligent-version-control) system."""

    TITLE = "IVC"
    CSS_PATH = "./tcss/ivc.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Chatbot()
        yield Footer()


if __name__ == "__main__":
    IVCApp().run()