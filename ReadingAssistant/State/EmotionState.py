import reflex as rx

from ReadingAssistant.Model.EmotionModel import Emotion
from datetime import datetime


class EmotionState(rx.State):
    latest_value: int

    def get_latest_emotion(self):
        with rx.session() as session:
            latest = session.exec(Emotion.select().order_by(Emotion.timestamp.desc())).first()
            if latest:
                self.latest_value = latest.value
                # self.latest_timestamp = latest.timestamp
            return self.latest_value#, self.latest_timestamp

    def on_load(self):
        return self.get_latest_emotion, 5 # 5 seconds