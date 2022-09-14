from brain_test import greeting, congratulation
from calc_logic import *
import prompt


def expression():
    greeting()
    print(BRAIN_CALC)
    index = 0
    winscore = 3
    while index != winscore:
        index += 1
        quest = calc()
        print("Question: ", quest)
        user_answer = prompt.string("Your answer: ")
        if user_answer == quest:
            print('Correct!')
            if index == winscore:
                congratulation()

            
        


expression()