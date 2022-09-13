#!/usr/bin/env python3
import prompt
from brain_games.scripts.logic import greeting, check_answer
from brain_games.scripts.games.brain_calc import expression
from brain_games.scripts.cli import welcome_user

user_name = ""

def greet():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}")
    return

def main():
    greet()

if __name__=='__main__':
    main()
