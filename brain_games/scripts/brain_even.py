#!/usr/bin/env/python

import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(
        f"Hello, {user_name}!\nAnswer 'yes' if the number is even, otherwise answer 'no'."
    )
    index = 0
    winscore = 3
    congrats = f"Congratulations, {user_name} !"
    while index < winscore:
        random_number = randint(1, 100)
        print("Question:", random_number)
        index += 1
        user_answer = prompt.string("Your answer: ")
        if (user_answer.lower() == "yes" and random_number % 2 == 0) or (
            user_answer.lower() == "no" and random_number % 2 != 0
        ):
            print("Correct!")
            if index == winscore:
                return congrats
        elif user_answer.lower() == "no" and random_number % 2 == 0:
            return (
                "no"
                " "
                f"is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {user_name}!"
            )
        elif user_answer.lower() == "yes" and random_number % 2 != 0:
            return (
                "yes"
                " "
                f"is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {user_name}!"
            )
        else:
            return f"{user_answer} is wrong answer ;(.\nLet's try again, {user_name}!"
