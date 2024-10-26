import json

import openai
from openai import OpenAI

# 设置API密钥
api_key = ""
client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key,
)


def generate_vocab_question(text):
    prompt = f"From the following text, create a multiple-choice question that asks the user to choose the sentence that best summarizes a paragraph or the entire text. Provide four options, with one being correct:\n\n{text}"
    prompt += '''provide the answer in {"question": "", "choices": {"0": "", "1": ""}, "correct_answer": "0"} format. Choices need to be numbered in sequence and make the correct answer random. Just give me json only.'''

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )

        return json.loads(response.choices[0].message.content)
    except Exception as e:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )

        return json.loads(response.choices[0].message.content)


def generate_true_false_question(text):
    prompt = f"From the following text, create a multiple-choice question that asks the user to choose the sentence that best summarizes a paragraph or the entire text. Provide four options, with one being correct:\n\n{text}"
    prompt += '''provide the answer in {"question": "", "choices": {"0": "", "1": ""}, "correct_answer": "0"} format. Choices need to be numbered in sequence and make the correct answer random. Just give me json only.'''
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )

        return json.loads(response.choices[0].message.content)
    except Exception as e:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )

        return json.loads(response.choices[0].message.content)


def generate_summary_question(text):
    prompt = f"From the following text, create a multiple-choice question that asks the user to choose the sentence that best summarizes a paragraph or the entire text. Provide four options, with one being correct:\n\n{text}"
    prompt += '''provide the answer in {"question": "", "choices": {"0": "", "1": ""}, "correct_answer": "0"} format. Choices need to be numbered in sequence and make the correct answer random. Just give me json only.'''
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )

        return json.loads(response.choices[0].message.content)
    except Exception as e:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )

        return json.loads(response.choices[0].message.content)


def generate_reference_question(text):
    prompt = f"From the following text, create a multiple-choice question that asks the user to choose the sentence that best summarizes a paragraph or the entire text. Provide four options, with one being correct:\n\n{text}"
    prompt += '''provide the answer in {"question": "", "choices": {"0": "", "1": ""}, "correct_answer": "0"} format. Choices need to be numbered in sequence and make the correct answer random. Just give me json only.'''
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )

        return json.loads(response.choices[0].message.content)
    except Exception as e:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )

        return json.loads(response.choices[0].message.content)


def generate_all_questions(text):
    questions = {}

    # 类型1：词汇题
    questions['vocab'] = generate_vocab_question(text)

    # 类型2：正确或错误的陈述
    questions['true_false'] = generate_true_false_question(text)

    # 类型3：段落总结题
    questions['summary'] = generate_summary_question(text)

    # 类型4：指示代词指代题
    questions['reference'] = generate_reference_question(text)

    return list(questions.values())


def provide_hint(question_type, step):
    hints = {
        'vocab': [
            "Here's an example sentence using the word.",
            "Here are example sentences using the options.",
            "Here is the definition of the word."
        ],
        'true_false': [
            "Here's the part of the text related to each option.",
            "Here are translations of the options.",
            "Here are translations of the relevant text portions."
        ],
        'summary': [
            "Here are translations of the options.",
            "Here is a translation of the paragraph.",
            "Here’s why the incorrect options are wrong."
        ],
        'reference': [
            "Here is a translation of the sentence.",
            "Here is a translation of the surrounding context.",
            "Here is the portion of the text that the pronoun refers to."
        ]
    }

    if step < len(hints[question_type]):
        return hints[question_type][step]
    else:
        pass






