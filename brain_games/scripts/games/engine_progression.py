import prompt, random
from brain_games.scripts.brain_test import greeting
from brain_games.scripts.progression_logic import *


def brain_prog():
    user_name = greeting()
    print(BRAIN_PROGRESSION)
    index = 0
    winscore = 3
    while index < winscore:
        index += 1
        question, correct_answer = progression()
        print('Question', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct!')
            if index == winscore:
                print(f"Congratulations, {user_name}")
        else:
            print(f"{user_answer}, is wrong answer :(. Correct answer was {correct_answer}.\nLet's try again, {user_name}")
            break
