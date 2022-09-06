import prompt


def greeting():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("What is the result of the expression?")
    congrats = f"Congratulations, {user_name}"
