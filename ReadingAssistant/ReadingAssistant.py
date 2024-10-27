import reflex as rx

from ReadingAssistant.API.EmotionAPI import update_emotion
from ReadingAssistant.Page import Index
from ReadingAssistant.State import ParagraphState


app = rx.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    ],
)
#app.add_page(Index.index, on_load=ParagraphState.ParagraphState.timer_task)
app.add_page(Index.index, on_load=ParagraphState.ParagraphState.timer_task)
app.api.add_api_route("/api/update_emotion", update_emotion, methods=["POST"])