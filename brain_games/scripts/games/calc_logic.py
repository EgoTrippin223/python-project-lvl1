import random, operator


BRAIN_CALC = 'What is the result of the expression?'



def calc():
    operator = ["-", "+", "*"]
    op = random.choice(operator)
    num1 = random.randint(10, 30)
    num2 = random.randint(1, 10)
    quest = f"{num1} {op} {num2}"
    if "+" == op:
        quest = str(num1 + num2)
    if "*" == op:
        quest = str(num1 * num2)
    if "-" == op:
        quest = str(num1 - num2)


calc()