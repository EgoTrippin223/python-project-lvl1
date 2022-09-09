import prompt
import math

def greeting():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")


def even(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"



def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return "no"
    return "yes"


def loop_function(function):
    for i in range(3):
        function()

def user_question(user_answer):
    user_answer = prompt.string("Your answer: ")