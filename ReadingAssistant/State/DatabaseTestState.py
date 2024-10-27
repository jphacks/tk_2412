import asyncio
from datetime import datetime

import reflex as rx

from ReadingAssistant.Model.EmotionModel import Emotion
from ReadingAssistant.State.EmotionState import EmotionState


class DatabaseTestState(rx.State):
    async def fetch_data(self):
        while True:
            with rx.session() as session:
                emotion = reversed(session.exec(Emotion.select().order_by(Emotion.timestamp.desc()).limit(5)).all())