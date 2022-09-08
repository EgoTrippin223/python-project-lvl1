from brain_games.scripts.logic import greeting
from brain_games.scripts.logic import even
import prompt
from random import randint


def is_even():
    index = 0
    winscore = 3
    greeting()
    print("Answer 'yes' if the number is even, otherwise answer 'no' ")
    while index < winscore:
        number = randint(1, 100)
        print("Question:", number)
        index += 1
        user_answer = prompt.string("Your answer: ")
        correct_answer = even(number)
        if user_answer.lower() == correct_answer:
            print("Correct!")
            if index == winscore:
                print("Congratulation!")
        else:
            print(
                f"{user_answer} is wrong answer :(. Correct answer was, {correct_answer}"
            )
            break
