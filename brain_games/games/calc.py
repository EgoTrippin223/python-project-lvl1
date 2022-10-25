import random


RULES = "What is the result of the expression?"
FIRST_NUM = random.randint(10, 30)
SECOND_NUM = random.randint(1, 10)

def get_question_and_answer():
    operation = ["-", "+", "*"]
    op = random.choice(operation)
    
    question = f"{FIRST_NUM} {op} {SECOND_NUM}"
    if "+" == op:
        correct_answer = str(FIRST_NUM + SECOND_NUM)
    if "*" == op:
        correct_answer = str(FIRST_NUM * SECOND_NUM)
    if "-" == op:
        correct_answer = str(FIRST_NUM - SECOND_NUM)
    return question, correct_answer
