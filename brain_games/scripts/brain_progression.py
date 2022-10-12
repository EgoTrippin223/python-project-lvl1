from brain_games.brain_engine import brain_engine
from brain_games.games.progression import get_question_and_answer
from brain_games.games.progression import BRAIN_TASK



def main():
    brain_engine(BRAIN_TASK, get_question_and_answer)



if __name__ == "__main__":
    main()