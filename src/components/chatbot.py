####################################################################################################
# Define chatbot components here.
####################################################################################################

from textual.app import ComposeResult
from textual.css.query import NoMatches
from textual.widgets import Static, Button, TextArea
from textual.containers import Container, Horizontal, Vertical, VerticalScroll


class QueryInput(Static):
    
    """A query input widget that takes input from the user."""

    BORDER_TITLE = "Enter your query here..."

    def on_mount(self) -> None:
        self.chatbot_query_area.border_title = self.BORDER_TITLE

    def compose(self) -> ComposeResult:
        self.chatbot_query_area = TextArea(id="chatbot_query_area")
        yield Horizontal(
            self.chatbot_query_area,
            Vertical(
                Button("Clear", id="chatbot_clear_button"),
                Button("Submit", id="chatbot_submit_button")
            )
        )

class Chatbot(Static):
    
    """A chatbot widget that serves as the main chatbot interface."""

    BORDER_TITLE = "Chatbot"
    USER_MESSAGE_BORDER_TITLE = "Me"
    CHATBOT_MESSAGE_BORDER_TITLE = "AI"
    INITIAL_DISPLAY_TEXT = "Your messages will appear here."
    INITIAL_DISPLAY_WIDGET = Static(INITIAL_DISPLAY_TEXT, id="chatbot_inital_display")

    def compose(self) -> ComposeResult:
        yield Vertical(
            VerticalScroll(
                self.INITIAL_DISPLAY_WIDGET,
                id="chatbot_display_area"
            ),
            QueryInput()
        )

    def clear_text_area(self) -> str:
        """Clear the text area and return the text."""
        chatbot_query_area = self.query_one("#chatbot_query_area", TextArea)
        text = chatbot_query_area.text
        chatbot_query_area.text = ""
        return text

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "chatbot_clear_button":
            self.clear_chatbot_display()
        elif event.button.id == "chatbot_submit_button":
            self.submit_chatbot_query()
    
    def submit_chatbot_query(self) -> None:
        """Submit a chat query."""
        # Get required widgets
        user_query = self.clear_text_area()
        if not user_query:
            return
        chatbot_display_area = self.query_one("#chatbot_display_area", VerticalScroll)
        try:
            chatbot_inital_display = self.query_one(
                "#chatbot_inital_display", Static)
        except NoMatches:
            chatbot_inital_display = None
        if chatbot_inital_display:
            chatbot_inital_display.remove()
            chatbot_display_area.styles.align = ("center", "bottom")
        # Set User message
        user_msg_body = Static(user_query,
                               classes="chatbot_user_msg_display")
        user_msg_body.border_title = self.USER_MESSAGE_BORDER_TITLE
        user_msg_widget = Container(
            user_msg_body, classes="chatbot_user_msg_container")
        # Set AI message
        ai_msg_body = Static(f"This is a test response - scroll = {chatbot_display_area.max_scroll_y}, {user_msg_widget.size[0]}", classes="chatbot_ai_msg_display")
        ai_msg_body.border_title = self.CHATBOT_MESSAGE_BORDER_TITLE
        ai_msg_widget = Container(ai_msg_body, classes="chatbot_ai_msg_container")
        # Mount messages
        chatbot_display_area.mount(user_msg_widget)
        chatbot_display_area.mount(ai_msg_widget)
        # Scroll to the end of the display
        chatbot_display_area.scroll_end()
    
    def clear_chatbot_display(self) -> None:
        """Clear the chat."""
        try:
            _ = self.query_one("#chatbot_inital_display", Static)
            self.clear_text_area()
            return
        except NoMatches:
            pass
        chatbot_display_area = self.query_one("#chatbot_display_area", VerticalScroll)
        chatbot_display_area.remove_children()
        chatbot_display_area.styles.align = ("center", "middle")
        chatbot_display_area.mount(self.INITIAL_DISPLAY_WIDGET)