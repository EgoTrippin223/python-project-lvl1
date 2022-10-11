from brain_games.calc_game import BRAIN_TASK
from brain_games.calc_game import get_question_and_answer
from brain_games.games.brain_engine import *


def main():
    brain_engine(get_question_and_answer, BRAIN_TASK)

if __name__=="__main__":
    main()