import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_answer}")

def set_difficulty():
    level = input("Choose a difficulty type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(logo)
    answer = random.randint(1, 100)
    print(answer)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")

        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of guesses! You lose!")
            return

game()