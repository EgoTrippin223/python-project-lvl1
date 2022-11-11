import random
from brain_games.brain_engine import MAX_VALUE


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    num = random.randint(0, MAX_VALUE)
    question_and_answer = (num, answer(num))
    return question_and_answer


def answer(number):
    if is_even(number):
        return "yes"
    else:
        return "no"


def is_even(number):
    return number % 2 == 0
