import prompt

ITERATIONS_NUMBER = 3  # кол-во вопросов игры
MAX_VALUE = 100


def brain_engine(BRAIN_TASK, question_and_answer):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(BRAIN_TASK)
    index = 0
    while index < ITERATIONS_NUMBER:
        index += 1
        (question, correct_answer) = question_and_answer()
        print("Question:", question)
        user_answer = prompt.string("Your answer: ")
        if user_answer == str(correct_answer):
            print("Correct!")
            if index == ITERATIONS_NUMBER:
                print(f"Congratulations, {name}!")
        else:
            print(
                f"{user_answer}, is wrong answer :(. Correct answer was {correct_answer}.\nLet's try again, {name}!"
            )
            break
