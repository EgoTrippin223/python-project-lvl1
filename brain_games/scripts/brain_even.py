from brain_games.games.even import BRAIN_TASK
from brain_games.games.even import get_question_and_answer
from brain_games.brain_engine import *


def main():
    brain_engine(get_question_and_answer, BRAIN_TASK)

if __name__=="__main__":
    main()