import random
from brain_games.brain_engine import MAX_VALUE

MIN_LENGTH = 5
MAX_LENGT = 10
STEP = 10
RULES = "What number is missing in the progression ?"


def get_question_and_answer():
    array = get_sequence()
    hidden_index = random.randint(0, len(array) - 1)
    question = (
        f"{' '.join(array[:hidden_index])} .. "
        f"{' '.join(array[hidden_index + 1:])}".strip()
    )
    answer = array[hidden_index]
    question_and_answer = (question, answer)
    return question_and_answer


def get_sequence():
    initial_term = random.randint(0, MAX_VALUE)
    number_of_terms = random.randint(MIN_LENGTH, MAX_LENGT)
    step = random.randint(1, STEP)
    last_term = initial_term + step * number_of_terms
    return [str(x) for x in range(initial_term, last_term, step)]
