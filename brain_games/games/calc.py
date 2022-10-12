import random


BRAIN_TASK = "What is the result of the expression?"


def get_question_and_answer():
    operation = ["-", "+", "*"]
    op = random.choice(operation)
    num1 = random.randint(10, 30)
    num2 = random.randint(1, 10)
    question = f"{num1} {op} {num2}"
    if "+" == op:
        correct_answer = str(num1 + num2)
    if "*" == op:
        correct_answer = str(num1 * num2)
    if "-" == op:
        correct_answer = str(num1 - num2)
    return question, correct_answer
