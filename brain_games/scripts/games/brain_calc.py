import prompt
from brain_games.scripts.brain_games import main
import random
from operator import add, sub, mul

#Математические выражения
add, sub, mul = '+', '-', '*'
op = random.choice(add, sub, mul)

beg1 = random.randint(1, 100)
beg2 = random.randint(1, 100)

def expression():
    print("What is the result of the expression?")
    index = 0
    winscore = 3
    op, function = random.choice(op)
    while index < winscore:
        index += 1
        user_answer = prompt.string("Your answer: ")
        answer = op(beg1, beg2)
        print ("Question:'{}{}{}?".format(beg1, op, beg2))
        


