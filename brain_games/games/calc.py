import random
from random import randint


RULES = "What is the result of the expression?"
MAX_VALUE_FIRST_NUM = 20
MAX_VALUE_SECOND_NUM = 10


def get_question_and_answer():
    operation = ["-", "+", "*"]
    op = random.choice(operation)
    first_num = randint(0, MAX_VALUE_FIRST_NUM)
    second_num = randint(1, MAX_VALUE_SECOND_NUM)
    question = f"{first_num} {op} {second_num}"
    if "+" == op:
        correct_answer = str(first_num + second_num)
    if "*" == op:
        correct_answer = str(first_num * second_num)
    if "-" == op:
        correct_answer = str(first_num - second_num)
    return question, correct_answer
