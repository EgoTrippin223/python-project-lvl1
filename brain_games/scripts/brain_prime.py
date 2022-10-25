from brain_games.brain_engine import start_game
from brain_games.games.prime import RULES
from brain_games.games.prime import get_question_and_answer


def main():
    start_game(RULES, get_question_and_answer)


if __name__ == "__main__":
    main()
