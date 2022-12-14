import random
from brain_games.brain_engine import MAX_VALUE

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    num = random.randint(2, MAX_VALUE)
    question_and_answer = (num, get_answer(num))
    return question_and_answer


def get_answer(number):
    if is_prime(number):
        return "yes"
    else:
        return "no"


def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
