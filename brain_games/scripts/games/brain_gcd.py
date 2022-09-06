import prompt
import random
import math
from brain_games.scripts.brain_games import greet


def gcd():
    greet()
    name = prompt.string("May I have your name ? ")
    print(f"Hello, {name}")
    print("Find the greatest common divisor of given numbers.")
    index = 0
    winscore = 3
    congrats = f"Congratulations, {name}"
    while index < winscore:
        index += 1
        num1 = random.randint(21, 99)
        num2 = random.randint(25, 63)
        quest = f"{num1}, {num2}"
        correct_answer = math.gcd(num1, num2)
        print("Question", quest)
        user_answer = prompt.string("Your answer: ")
        if user_answer == str(correct_answer):
            print("Correct!")
            if index == winscore:
                print(congrats)
        else:
            print(
                f"{user_answer} is wrong answer ;(.\nCorrect answer was,",
                correct_answer,
            )
            break
