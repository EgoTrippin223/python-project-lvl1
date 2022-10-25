import random
from brain_games.brain_engine import MAX_VALUE


RULES = "What number is missing in the progression ?"

def get_question_and_answer():
    numbers = []
    FIRST_NUM = random.randint(1, 5)
    SECOND_NUM = random.randint(30, 45)
    STEP = random.randint(2, 4)
    for i in range(FIRST_NUM, SECOND_NUM, STEP):
        numbers.append(i)
    correct_answer = random.choice(numbers)
    index_x = numbers.index(correct_answer)
    numbers[index_x] = ".."
    question = " ".join(map(str, numbers))
    question_and_answer = (question, correct_answer)
    return question_and_answer