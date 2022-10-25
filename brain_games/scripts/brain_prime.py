from brain_games import brain_engine
from brain_games.games.prime import RULES
from brain_games.games.prime import get_question_and_answer


def main():
    brain_engine.start_game(RULES, get_question_and_answer)


if __name__ == "__main__":
    main()
