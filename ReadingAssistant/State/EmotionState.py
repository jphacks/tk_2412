import reflex as rx

from ReadingAssistant.Model.EmotionModel import Emotion
from ReadingAssistant.Utils.utils_function import use_model
from ReadingAssistant.Utils.train_model import Emotion_MLP

class EmotionState(rx.State):

    async def get_latest_emotion(self):
        with rx.session() as session:
            emotions = list(reversed(session.exec(Emotion.select().order_by(Emotion.timestamp.desc()).limit(5)).all()))
            inputs = []

            if len(emotions) == 5:
                for i in emotions:
                    inputs.append(i.value)

            emotion = use_model(inputs)
            print(emotion)