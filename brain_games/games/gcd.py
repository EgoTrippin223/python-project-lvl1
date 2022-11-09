from random import randint
import math


RULES = "Find the greatest common divisor of given numbers."
MAX_VALUE_FIRST_NUM = 99
MIN_VALUE_FIRST_NUM = 25
MAX_VALUE_SECOND_NUM = 63
MIN_VALUE_SECOND_NUM = 25


def get_question_and_answer():
    num_1 = randint(MIN_VALUE_FIRST_NUM, MAX_VALUE_FIRST_NUM)
    num_2 = randint(MIN_VALUE_SECOND_NUM, MAX_VALUE_SECOND_NUM)
    question_and_answer = (f"{num_1} {num_2}", str(gcd(num_1, num_2)))
    return question_and_answer


def gcd(number1, number2):
    return math.gcd(number1, number2)
