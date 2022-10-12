from random import randint
import math


BRAIN_TASK = "Find the greatest common divisor of given numbers."


def get_question_and_answer():
    num1 = randint(21, 99)
    num2 = randint(25, 63)
    question = f"{num1} {num2}"
    correct_answer = math.gcd(num1, num2)
    return question, correct_answer
