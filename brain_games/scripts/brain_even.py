from brain_games.games.even import RULES
from brain_games.games.even import get_question_and_answer
from brain_games import brain_engine


def main():
    brain_engine.start_game(RULES, get_question_and_answer)


if __name__ == "__main__":
    main()
