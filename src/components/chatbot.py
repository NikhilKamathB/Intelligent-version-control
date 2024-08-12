####################################################################################################
# Define chatbot components here.
####################################################################################################

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Button, TextArea


class QueryInput(Static):
    
    """A query input widget that takes input from the user."""

    BORDER_TITLE = "Enter your query here..."

    def compose(self) -> ComposeResult:
        yield Horizontal(
            TextArea(),
            Vertical(
                Button("Send")
            )
        )


class Chatbot(Static):
    
    """A chatbot widget that serves as the main chatbot interface."""

    BORDER_TITLE = "Chatbot"

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static("One"),
            QueryInput()
        )