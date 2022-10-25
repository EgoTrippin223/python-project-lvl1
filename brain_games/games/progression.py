import random
from brain_games.brain_engine import MAX_VALUE


RULES = "What number is missing in the progression ?"

def get_question_and_answer():
    numbers = []
    MIN_LENGTH = 5
    MAX_LENGT = 10
    STEP = 10
    for i in range(MIN_LENGTH, MAX_LENGT, STEP):
        numbers.append(i)
    index_x = numbers.index(question_and_answer)
    numbers[index_x] = ".."
    question_and_answer = " ".join(map(str, numbers)), random.choice(numbers)
    return question_and_answer