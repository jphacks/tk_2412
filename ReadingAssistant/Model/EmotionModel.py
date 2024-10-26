from datetime import datetime

import reflex as rx

class Emotion(rx.Model, table=True):
    value: int
    timestamp: datetime