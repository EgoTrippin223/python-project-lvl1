from brain_games.brain_engine import brain_engine
from brain_games.games.prime import BRAIN_TASK
from brain_games.games.prime import get_question_and_answer



def main():
    brain_engine(BRAIN_TASK, get_question_and_answer)


if __name__ == "__main__":
    main()