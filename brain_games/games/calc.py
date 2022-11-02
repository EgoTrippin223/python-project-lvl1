import random
from random import randint


RULES = "What is the result of the expression?"
MAX_VALUE_FIRST_NUM = 20
MAX_VALUE_SECOND_NUM = 10


def get_question_and_answer():
    operation = ["-", "+", "*"]
    op = random.choice(operation)
    FIRST_NUM = randint(0, MAX_VALUE_FIRST_NUM)
    SECOND_NUM = randint(1, MAX_VALUE_SECOND_NUM)
    question = f"{FIRST_NUM} {op} {SECOND_NUM}"
    if "+" == op:
        correct_answer = str(FIRST_NUM + SECOND_NUM)
    if "*" == op:
        correct_answer = str(FIRST_NUM * SECOND_NUM)
    if "-" == op:
        correct_answer = str(FIRST_NUM - SECOND_NUM)
    return question, correct_answer
