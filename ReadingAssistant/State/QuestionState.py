import reflex as rx
from typing import List

class QuestionState(rx.State):
    q_index: int = 0
    questions: List[dict[str, str]] = [{}]
    choices: List[dict[str, str]] = [{}]
    is_loading: bool = False
    q_percent: int = 0

    def minus_index(self):
        self.q_index -= 1
        if self.q_index < 0:
            self.q_index = 0
        self.q_percent = ((self.q_index + 1) * 100) // len(self.choices)

    def plus_index(self):
        self.q_index += 1
        if self.q_index >= len(self.choices):
            self.q_index = len(self.choices) - 1
        self.q_percent = ((self.q_index + 1) * 100) // len(self.choices)