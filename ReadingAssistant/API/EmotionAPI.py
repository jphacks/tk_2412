from datetime import datetime
import reflex as rx

from ReadingAssistant.Model.EmotionModel import Emotion


async def update_emotion(value: int):
    with rx.session() as session:
        new_sensor_value = Emotion(value=value, timestamp=datetime.now())
        session.add(new_sensor_value)
        session.commit()
        return {"status": "success"}
    return {"status": "failed"}