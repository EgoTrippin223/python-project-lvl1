import prompt
import random


def progression():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May i have your name? ")
    print("What number is missing in the progression?")
    index = 0
    winscore = 3
    congrats = f"Congratulations, {user_name}!"
    while index < winscore:
        index += 1
        numbers = []
        num1 = random.randint(1, 2)
        num2 = random.randint(15, 20)
        n = random.randint(2, 3)
        for i in range(num1, num2, n):
            numbers.append(i)
        numbers.sort
        correct_answer = random.choice(numbers)
        index_x = numbers.index(correct_answer)
        numbers[index_x] = ".."
        question = " ".join(map(str, numbers))
        print("Question:", question)
        user_answer = prompt.string("Your answer: ")
        if str(user_answer) == str(correct_answer):
            print("Correct!")
            if index == winscore:
                print(congrats)
        else:
            print(
                f"{user_answer} is wrong answer ;(.\nCorrect answer was,",
                correct_answer,
            )
            break
