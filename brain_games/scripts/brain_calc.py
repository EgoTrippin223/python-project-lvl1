from brain_games.games.calc import RULES
from brain_games.games.calc import get_question_and_answer
from brain_games.brain_engine import start_game


def main():
    start_game(RULES, get_question_and_answer)


if __name__ == "__main__":
    main()
