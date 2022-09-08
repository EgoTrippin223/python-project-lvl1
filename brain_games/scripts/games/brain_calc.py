from brain_games.scripts.logic import greeting

import prompt
import random
import operator


def expression():
    greeting()
    print('What is the result of the expression?')
    index = 0
    winscore = 3
    while index < winscore:
        operator = ["-", "+", "*"]
        op = random.choice(operator)
        num1 = random.randint(10, 30)
        num2 = random.randint(1, 10)
        index += 1
        quest = f"{num1} {op} {num2}"
        print("Question:", quest)
        user_answer = prompt.string("Your answer: ")
        if "+" == op:
            quest = str(num1 + num2)
        if "-" == op:
            quest = str(num1 - num2)
        if "*" == op:
            quest = str(num1 * num2)
        if user_answer == str(quest):
            print('Correct!')
            if index == winscore:
                print("Congratulation!")
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was,", quest)
            break
