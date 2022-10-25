from brain_games.brain_engine import start_game
from brain_games.games.progression import get_question_and_answer
from brain_games.games.progression import BRAIN_TASK


def main():
    start_game(BRAIN_TASK, get_question_and_answer)


if __name__ == "__main__":
    main()
