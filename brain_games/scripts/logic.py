import prompt
import math


user_name = ""

def greeting():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")


def checker(answer, answer_in, score):
    if answer == answer_in:
        print('Correct!')
        a = score[0]
        a += 1
        score[0] = a


def congratulation():
    print(f"Congratulations, {user_name}!")


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
    return


def user_question():
    user_answer = prompt.string('Your answer: ')

