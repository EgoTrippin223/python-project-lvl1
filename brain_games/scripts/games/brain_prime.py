from random import randint
import prompt
from brain_games.scripts.logic import is_prime, congratulation, check_answer, greeting


def prime():
    greeting()
    index = 0
    winscore = 3
    while index != winscore:
        index += 1
        number = randint(2, 100)
        correct_answer = is_prime(number)
        print(f"Question: {number}")
        user_answer = prompt.string(f"Your answer: ")
        check_answer(user_answer, correct_answer)
        if index == winscore:
            congratulation()
        if user_answer != correct_answer:
            break
prime()