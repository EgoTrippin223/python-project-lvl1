import prompt
from brain_games.scripts.brain_test import greeting
from brain_games.scripts.prime_logic import is_prime
from random import randint


def brain_prime():
    user_name = greeting()
    index = 0
    winscore = 3
    while index != winscore:
        index += 1
        num = randint(2, 100)
        correct_answer = is_prime(num)
        print('Question:', num)
        user_answer = prompt.string('Your answer: ')
        if user_answer.lower() == correct_answer:
            print('Correct!')
            if index == winscore:
                print(f'Congratulations, {user_name}')

        else:
            print(f"{user_answer}, is wrong answer :(. Correct answer was {is_prime(num)}.\nLet's try again, {user_name}")
            break
