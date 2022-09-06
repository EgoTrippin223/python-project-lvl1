import prompt
from random import randint


def greeting_prime():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May i have your name? ")
    print(f"Hello, {user_name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    congrats = print(f"Congratulations, {user_name}")


def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return "no"
    return "yes"
