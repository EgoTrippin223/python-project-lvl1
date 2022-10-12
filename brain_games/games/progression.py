import random


BRAIN_TASK = "What number is missing in the progression ?"


def get_question_and_answer():
    numbers = []
    num1 = random.randint(1, 5)
    num2 = random.randint(30, 45)
    n = random.randint(2, 4)
    for i in range(num1, num2, n):
        numbers.append(i)
    correct_answer = random.choice(numbers)
    index_x = numbers.index(correct_answer)
    numbers[index_x] = ".."
    question = " ".join(map(str, numbers))
    return question, correct_answer
