import random
from random import randint
from brain_games.brain_engine import MAX_VALUE


RULES = "What number is missing in the progression ?"
MIN_LENGTH_SEQUENCE = 5
MAX_LENGTH_SEQUENCE = 10
DIFFERENCE = 10


def get_question_and_answer():
    initial_term = randint(0, MAX_VALUE)
    number_of_terms = randint(MIN_LENGTH_SEQUENCE, MAX_LENGTH_SEQUENCE)
    difference = randint(1, DIFFERENCE)
    progression = arithm_sequence(initial_term, number_of_terms, difference)
    correct_answer = random.choice(progression)
    index_x = progression.index(correct_answer)
    progression[index_x] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer


def arithm_sequence(initial_term, number_of_terms, difference):
    last_term = initial_term + difference * number_of_terms
    progression = list(range(initial_term, last_term, difference))
    return progression
