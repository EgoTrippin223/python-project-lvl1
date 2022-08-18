import prompt
import random
import operator


def expression():

    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print("What is the result of the expression?")
    index = 0
    winscore = 3
    congrats = f"Congratulations, {user_name}"
    while index < winscore:
        operator = ["-", "+", "*"]
        op = random.choice(operator)
        num1 = random.randint(10, 30)
        num2 = random.randint(1, 10)
        answer = f"{num1} {op} {num2}"
        index += 1
        print("Question:", answer)
        user_answer = prompt.string("Your answer: ")
        if "+" == op:
            answer = str(num1 + num2)
        if "-" == op:
            answer = str(num1 - num2)
        if "*" == op:
            answer = str(num1 * num2)
        if user_answer == answer:
            print("Correct!")
            if index == winscore:
                print(congrats)
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was,", answer)
            break
