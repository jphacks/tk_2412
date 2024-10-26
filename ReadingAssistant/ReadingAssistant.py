import reflex as rx
from ReadingAssistant.Page import Index
from ReadingAssistant.State import ParagraphState


app = rx.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    ],
)
app.add_page(Index.index, on_load=ParagraphState.ParagraphState.timer_task)
# app.api.add_api_route("/update_heart_rate", update_heart_rate, methods=["POST"])