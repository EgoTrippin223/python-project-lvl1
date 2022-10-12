import random
from brain_games.brain_engine import MAX_VALUE


BRAIN_TASK = "Answer 'yes' if the number is even, otherwise answer 'no' "

def get_question_and_answer():
    rand = random.randint(0, MAX_VALUE)
    question = rand
    if rand % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
