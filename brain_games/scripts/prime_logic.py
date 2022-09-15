from ast import Num
import random
from random import randint


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "no"
    return "yes"