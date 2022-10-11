import prompt
from brain_games.brain_test import greeting


def brain_engine(question_and_answer, BRAIN_TASK):
    user_name = greeting()
    print(BRAIN_TASK)
    index = 0
    winscore = 3
    while index < winscore:
        index += 1
        (question, correct_answer) = question_and_answer()
        print('Question', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct!')
            if index == winscore:
                print(f"Congratulations, {user_name}")
        else:
            print(f"{user_answer}, is wrong answer :(. Correct answer was {correct_answer}.\nLet's try again, {user_name}")
            break
