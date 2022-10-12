from brain_games.brain_engine import *
from brain_games.games.gcd import get_question_and_answer
from brain_games.games.gcd import BRAIN_TASK




def main():
    brain_engine(get_question_and_answer, BRAIN_TASK)



if __name__ == "__main__":
    main()