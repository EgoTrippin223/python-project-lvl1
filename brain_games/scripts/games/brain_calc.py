from brain_games.scripts.logic import greeting, check_answer, congratulation

import prompt
import random
import operator


def expression():
    greeting()
    print('What is the result of the expression?')
    index = 0
    winscore = 3
    while index != winscore:
        index += 1
        operator = ["-", "+", "*"]
        op = random.choice(operator)
        num1 = random.randint(10, 30)
        num2 = random.randint(1, 10)
        quest = f"{num1} {op} {num2}"
        print("Question:", quest)
        user_answer = prompt.string("Your answer: ")
        if "+" == op:
            quest = str(num1 + num2)
        if "-" == op:
            quest = str(num1 - num2)
        if "*" == op:
            quest = str(num1 * num2)
        check_answer(user_answer, quest)
        if index == winscore:
            congratulation()
        if user_answer != quest:
            break
            
        


expression()