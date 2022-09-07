#!/usr/bin/env/python
from logic_even import greeting
from logic_even import even
import prompt
from random import randint


def is_even():
    index = 0
    winscore = 3
    greeting()
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
is_even()