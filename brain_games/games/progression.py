import random


RULES = "What number is missing in the progression ?"


def prog():
    FIRST_NUM = random.randint(1, 5)
    SECOND_NUM = random.randint(30, 35)
    STEP = random.randint(2, 3)
    progression = list(range(FIRST_NUM, SECOND_NUM, STEP))
    return progression


def get_question_and_answer():
    progression = prog()
    correct_answer = random.choice(progression)
    index_x = progression.index(correct_answer)
    progression[index_x] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer
