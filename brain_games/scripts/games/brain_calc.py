import prompt
import random
import operator
from logic_calc import greeting


def expression():
    greeting()
    index = 0
    winscore = 3
    while index < winscore:
        operator = ["-", "+", "*"]
        op = random.choice(operator)
        num1 = random.randint(10, 30)
        num2 = random.randint(1, 10)
        index += 1
        answer = f"{num1} {op} {num2}"
        print("Question:", answer)
        user_answer = prompt.string("Your answer: ")
        if "+" == op:
            answer = str(num1 + num2)
        if "-" == op:
            answer = str(num1 - num2)
        if "*" == op:
            answer = str(num1 * num2)
        if user_answer == str(answer):
            print("Correct!")
            if index == winscore:
                print("Congratulation!")
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was,", answer)
            break


expression()
