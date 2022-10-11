from random import randint

BRAIN_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    num = randint(2, 100)
    question = num
    correct_answer = "yes"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            correct_answer = "no"
            break
    return question, correct_answer
