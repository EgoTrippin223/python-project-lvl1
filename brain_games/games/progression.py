import random
from random import randint


RULES = "What number is missing in the progression ?"
MIN_FIRST_MEMBER_OF_SEQUENCE = 1
MAX_FIRST_MEMBER_OF_SEQUENCE = 5
MIN_SECOND_MEMBER_OF_SEQUENCE = 30
MAX_SECOND_MEMBER_OF_SEQUENCE = 35
MIN_VALUE_STEP = 2
MAX_VALUE_STEP = 3


def sequence():
    FIRST_NUM = randint(MIN_FIRST_MEMBER_OF_SEQUENCE, MAX_FIRST_MEMBER_OF_SEQUENCE)
    SECOND_NUM = randint(MIN_SECOND_MEMBER_OF_SEQUENCE, MAX_SECOND_MEMBER_OF_SEQUENCE)
    STEP = randint(MIN_VALUE_STEP, MAX_VALUE_STEP)
    progression = list(range(FIRST_NUM, SECOND_NUM, STEP))
    return progression


def get_question_and_answer():
    progression = sequence()
    correct_answer = random.choice(progression)
    index_x = progression.index(correct_answer)
    progression[index_x] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer
