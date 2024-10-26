import reflex as rx
from ReadingAssistant.State.QuestionState import QuestionState

class FormRadioState(rx.State):
    form_data: dict = {}

    async def handle_submit(self, form_data: dict):
        self.form_data = form_data
        qs = await self.get_state(QuestionState)
        return self.show_toast(str(form_data["option"]) == str(qs.questions[qs.q_index]["answer"]))


    def show_toast(self, is_correct: bool = False):
        if not is_correct:
            return rx.toast.error(
            "emmmm",
            position="top-right",
        )
        return rx.toast.success(
            "6",
            position="top-right",
        )