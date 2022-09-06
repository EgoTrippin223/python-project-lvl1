from random import randint
import prompt
from logic_prime import is_prime
from logic_prime import greeting_prime


def prime():
    greeting_prime()
    index = 0
    winscore = 3
    while index != winscore:
        number = randint(2, 100)
        correct_answer = is_prime(number)
        print(f"Question: {number}")
        user_answer = prompt.string(f"Your answer: ")
        if user_answer.lower() == correct_answer:
            print("Correct!")
            index += 1
            if index == winscore:
                print("Congratulations!")
        else:
            print(
                f"{user_answer}, is wrong answer, correct answer was {correct_answer}"
            )
            break
    else:
        return 0
