import reflex as rx
import nltk
from typing import List

from ReadingAssistant.State import QuestionState
from ReadingAssistant.Utils import question_prompt_experiment
import asyncio
import random
import time

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')


class ParagraphState(rx.State):
    my_paragraphs: List[str] = []
    is_loading: bool = False
    reading_time_int: int = 0
    timer_running: bool = False
    timer_exist = False
    _n_tasks: int = 0

    @rx.background
    async def timer_task(self):
        async with self:
            self._n_tasks += 1
            my_number = self._n_tasks

        while True:
            async with self:
                if my_number != self._n_tasks:
                    # only preserve the latest timer
                    return
                if self.timer_running:
                    self.reading_time_int += 1

            await asyncio.sleep(1)

    def toggle_running(self):
        self.timer_running = not self.timer_running
        if self.timer_running:
            return ParagraphState.timer_task

    @rx.var(cache=False)
    def reading_time(self):
        return "{:02d}:{:02d}".format(self.reading_time_int // 60, self.reading_time_int % 60)

    @rx.var(cache=False)
    def my_paragraphs_empty(self):
        return self.my_paragraphs == [] or self.my_paragraphs == [""]

    def generate_tokens(self):
        self.is_loading = True
        yield
        rt = self.my_paragraphs_tokens
        self.is_loading = False
        return rt

    @rx.var(cache=False)
    def my_paragraphs_tokens(self) -> List[List[str]]:
        return_value = [
            nltk.pos_tag(nltk.word_tokenize(paragraph))
            for paragraph in self.my_paragraphs
        ]
        return return_value

    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            self.is_loading = True
            qs = await self.get_state(QuestionState.QuestionState)
            qs.is_loading = True
            self.timer_running = False
            yield
            upload_data = await file.read()
            passage = upload_data.decode("utf-8")
            questions = []
            choices = []
            for q in question_prompt_experiment.generate_all_questions(passage):
                random.seed(time.time())
                correct_answer = str(random.randint(0, len(q["choices"]) - 1))
                temp_answer = q["choices"][correct_answer]
                q["choices"][correct_answer] = q["choices"]["0"]
                q["choices"]["0"] = temp_answer
                questions.append({"question": q["question"], "answer": correct_answer})
                choices.append(q["choices"])
            qs.questions = questions
            qs.choices = choices
            qs.q_percent = 100 // len(questions)
            self.is_loading = False
            qs.is_loading = False
            # change here to += for multi file situation
            self.my_paragraphs = passage.split("\n")
            self.reading_time_int = 0
            self.timer_running = True


def display_word(word: str, tag: str):
    return rx.match(
        tag,
        # ("IN", rx.badge(word, color_scheme="blue")),  # 介词
        # ("VB", rx.badge(word, color_scheme="red")),  # 动词 (base form)
        # ("VBD", rx.badge(word, color_scheme="green")),  # 动词 (过去式)
        # ("VBG", rx.badge(word, color_scheme="yellow")),  # 动词 (现在分词)
        # ("VBN", rx.badge(word, color_scheme="purple")),  # 动词 (过去分词)
        # ("VBZ", rx.badge(word, color_scheme="orange")),  # 动词 (单数第三人称)
        ("NN", rx.badge(word, color_scheme="brown")),  # 名词 (单数)
        ("NNS", rx.badge(word, color_scheme="amber")),  # 名词 (复数)
        # ("JJ", rx.badge(word, color_scheme="lime")),  # 形容词
        # ("JJR", rx.badge(word, color_scheme="sky")),  # 比较级形容词
        # ("JJS", rx.badge(word, color_scheme="gold")),  # 最高级形容词
        # ("RB", rx.badge(word, color_scheme="cyan")),  # 副词
        # ("RBR", rx.badge(word, color_scheme="crimson")),  # 比较级副词
        # ("RBS", rx.badge(word, color_scheme="violet")),  # 最高级副词
        # ("PRP", rx.badge(word, color_scheme="plum")),  # 人称代词
        # ("PRP$", rx.badge(word, color_scheme="jade")),  # 物主代词
        # ("DT", rx.badge(word, color_scheme="indigo")),  # 限定词
        # ("CD", rx.badge(word, color_scheme="teal")),  # 基数词
        # ("UH", rx.badge(word, color_scheme="tomato")),  # 感叹词
        rx.text(word, size="2")
    )


def display_paragraph(paragraph_tokens: List[str]):
    return rx.flex(
        rx.foreach(
            paragraph_tokens,
            lambda word_tag: display_word(word_tag[0], word_tag[1])
        ),
        width="38vw",
        wrap="wrap",
        spacing="1",
    )


def text_with_badges():
    return rx.vstack(
        rx.foreach(
            ParagraphState.my_paragraphs_tokens,
            lambda paragraph_tokens: rx.vstack(
                display_paragraph(paragraph_tokens),
                rx.spacer()
            )
        ),
        width="40vw",
    )