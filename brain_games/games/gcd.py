from random import randint
import math


RULES = "Find the greatest common divisor of given numbers."


def get_question_and_answer():
    NUM1 = randint(21, 99)
    NUM2 = randint(25, 63)
    question_and_answer = (f"{NUM1} {NUM2}", str(gcd(NUM1, NUM2)))
    return question_and_answer


def gcd(number1, number2):
    return math.gcd(number1, number2)
