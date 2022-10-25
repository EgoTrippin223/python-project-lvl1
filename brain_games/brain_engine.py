import prompt

ITERATIONS_NUMBER = 3  # кол-во вопросов игры
MAX_VALUE = 100


def start_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.RULES)
    index = 0
    while index < ITERATIONS_NUMBER:
        index += 1
        (question, correct_answer) = game.get_question_and_answer()
        print("Question:", question)
        user_answer = prompt.string("Your answer: ")
        if user_answer == str(correct_answer):
            print("Correct!")
            if index == ITERATIONS_NUMBER:
                print(f"Congratulations, {name}!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
                f"\nLet's try again, {name}!"
            )
            break
