import prompt
import random
from brain_games.scripts.logic import greeting, check_answer, congratulation

def progression():
    greeting()
    print("What number is missing in the progression?")
    index = 0
    winscore = 3
    while index < winscore:
        index += 1
        numbers = []
        num1 = random.randint(1, 5)
        num2 = random.randint(15, 25)
        n = random.randint(1, 3)
        for i in range(num1, num2, n):
            numbers.append(i)
        numbers.sort
        correct_answer = random.choice(numbers)
        index_x = numbers.index(correct_answer)
        numbers[index_x] = ".."
        question = " ".join(map(str, numbers))
        print("Question:", question)
        user_answer = prompt.string("Your answer: ")
        check_answer(user_answer, numbers[".."])
        if index == winscore:
                congratulation()
        if user_answer != question:
            break
progression()