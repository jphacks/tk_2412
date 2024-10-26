import reflex as rx

class EmotionState(rx.State):
    emotion: float = 0

    def get_latest_emotion(self):
        with rx.session() as session:
            latest = session.exec(Emotion.select().order_by(Emotion.timestamp.desc())).first()
            if latest:
                self.emotion = latest.value

    def on_load(self):
        return self.get_latest_emotion, 5 # 5 seconds