from brain_games.games.calc import BRAIN_TASK
from brain_games.games.calc import get_question_and_answer
from brain_games.brain_engine import *


def main():
    brain_engine(BRAIN_TASK, get_question_and_answer)


if __name__ == "__main__":
    main()
