import random
from brain_games.brain_engine import MAX_VALUE


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    rand = random.randint(0, MAX_VALUE)
    question_and_answer = (rand, is_even(rand) and "yes" or "no")
    return question_and_answer


def is_even(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"
