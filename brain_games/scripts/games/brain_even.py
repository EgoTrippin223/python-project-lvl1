from brain_games.scripts.logic import (even, greeting,
                check_answer, congratulation)
import prompt
from random import randint


def is_even():
    index = 0
    winscore = 3
    greeting()
    print("Answer 'yes' if the number is even, otherwise answer 'no' ")
    while index != winscore:
        number = randint(1, 100)
        index += 1
        print("Question:", number)
        user_answer = prompt.string("Your answer: ")
        correct_answer = even(number)
        check_answer(user_answer, correct_answer)
        if index == winscore:
            congratulation()
        if user_answer != correct_answer:
            break
        

is_even()