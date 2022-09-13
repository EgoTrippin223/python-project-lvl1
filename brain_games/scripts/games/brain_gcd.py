import prompt
import random
import math
from brain_games.scripts.logic import greeting, check_answer, congratulation


def gcd():
    greeting()
    print("Find the greatest common divisor of given numbers.")
    index = 0
    winscore = 3
    while index < winscore:
        index += 1
        num1 = random.randint(21, 99)
        num2 = random.randint(25, 63)
        quest = f"{num1}, {num2}"
        correct_answer = math.gcd(num1, num2)
        print("Question", quest)
        user_answer = prompt.string("Your answer: ")
        check_answer(user_answer, correct_answer)
        if index == winscore:congratulation()
gcd()