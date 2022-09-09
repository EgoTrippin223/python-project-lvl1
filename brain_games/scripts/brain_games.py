#!/usr/bin/env python3
import prompt

from brain_games.scripts.cli import welcome_user


def greet():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")


def main():
    greet()

if __name__=='__main__':
    main()
