from random import randint
import math


RULES = "Find the greatest common divisor of given numbers."


def get_question_and_answer():
    num1 = randint(21, 99)
    num2 = randint(25, 63)
    question_and_answer = (f"{num1} {num2}", str(gcd(num1, num2)))
    return question_and_answer


def gcd(number1, number2):
    return math.gcd(number1, number2)
