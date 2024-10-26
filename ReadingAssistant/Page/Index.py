import reflex as rx
from ReadingAssistant.State import ParagraphState
from ReadingAssistant.State import QuestionState
from ReadingAssistant.State import FormRadioState

def reading_area() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.heading("Reading Area", color="lightblue", size="9"),
            rx.flex(
                rx.heading(
                    ParagraphState.ParagraphState.reading_time,
                    color="red",
                    size="4",
                    height="auto",
                    flex_wrap="wrap"
                ),
                justify="center",
                align="center",
                height="auto",
                flex_wrap="wrap"
            ),
            justify="between",
            width="100%",
            height="auto",
            flex_wrap="wrap",
        ),
        rx.divider(width="100%"),
        rx.card(
            rx.upload(
                rx.flex(
                    rx.cond(
                        ParagraphState.ParagraphState.is_loading,
                        rx.spinner(size="3"),
                        rx.cond(
                            ParagraphState.ParagraphState.my_paragraphs_empty,
                            rx.text("Drag and drop files here or click to select files"),
                            rx.scroll_area(
                                rx.flex(
                                    ParagraphState.text_with_badges(),
                                    direction="column",
                                    spacing="1",
                                ),
                                type="hover",
                                scrollbars="vertical",
                            ),
                        ),
                    ),
                    height="100%",
                    justify="center",
                    align="center",
                    wrap="wrap",
                    direction="column",
                ),
                padding="5px",
                multiple=True,
                accept={
                    # "application/pdf": [".pdf"],
                    # "image/png": [".png"],
                    # "image/jpeg": [".jpg", ".jpeg"],
                    # "image/gif": [".gif"],
                    # "image/webp": [".webp"],
                    # "text/html": [".html", ".htm"],
                    "text/plain": [".txt", ".text"],
                },
                max_files=1,
                disabled=False,
                on_drop=ParagraphState.ParagraphState.handle_upload(
                    rx.upload_files(upload_id="upload")
                ),
                id="upload",
                height="100%",
            ),
            width="40vw",
            height="40vh",
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
        width="50vw",
    )


def question_area() -> rx.Component:
    return rx.vstack(
        rx.heading("Question Area", size="9", color="lightgreen"),
        rx.divider(width="100%"),
        rx.card(
            rx.cond(
                QuestionState.QuestionState.is_loading,
                rx.flex(
                    rx.spinner(size="3"),
                    width="100%",
                    height="100%",
                    justify="center",
                    align="center",
                    wrap="wrap",
                ),
                rx.flex(
                    rx.form(
                        rx.flex(
                            rx.flex(
                                rx.scroll_area(
                                    rx.text(QuestionState.QuestionState.questions[
                                                QuestionState.QuestionState.q_index]["question"]),
                                ),
                                height="3vh",
                            ),
                            rx.spacer(),
                            rx.divider(width="100%"),
                            rx.spacer(),
                            rx.scroll_area(
                                rx.radio_cards.root(
                                    rx.flex(
                                        rx.foreach(
                                            QuestionState.QuestionState.choices[
                                                QuestionState.QuestionState.q_index],
                                            lambda question: rx.radio_cards.item(question[1],
                                                                                 value=question[0]),
                                        ),
                                        direction="column",
                                        spacing="4",
                                        # this is quite ugly
                                        align="start",
                                    ),
                                    name="option",
                                    type="hover",
                                    scrollbars="vertical",
                                    default_value="0",
                                    width="37vw",
                                ),
                                height="28vh",
                            ),
                            rx.spacer(),
                            # rx.divider(width="100%"),
                            rx.progress(value=QuestionState.QuestionState.q_percent),
                            rx.spacer(),
                            rx.flex(
                                rx.button(
                                    rx.icon("arrow-left"),
                                    type="button",
                                    variant="ghost",
                                    on_click=QuestionState.QuestionState.minus_index,
                                ),
                                rx.spacer(),
                                rx.button(
                                    rx.icon("check"),
                                    type="submit",
                                    variant="outline",
                                ),
                                rx.spacer(),
                                rx.button(
                                    rx.icon("arrow-right"),
                                    type="button",
                                    variant="ghost",
                                    on_click=QuestionState.QuestionState.plus_index,
                                ),
                                width="100%",
                                height="5vh",
                            ),
                            rx.spacer(),
                            height="40vh",
                            justify="between",
                            # align="center",
                            direction="column",
                        ),
                        on_submit=FormRadioState.FormRadioState.handle_submit,
                        reset_on_submit=True,
                        height="40vh",
                    ),
                    spacing="5",
                    justify="between",
                    direction="column",
                    align="center",
                    wrap="wrap",
                    height="40vh",
                ),
            ),
            width="40vw",
            height="40vh",
            align="center",
            justify="center",
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
        width="50vw",
    )


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.container(
            rx.flex(
                reading_area(),
                question_area(),
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
        ),
    )