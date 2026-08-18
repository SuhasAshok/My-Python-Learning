import random
from game_data import data
from art import logo, vs

def compare(option_a, option_b):
    if option_a > option_b:
        return "a"
    else:
        return "b"

def game():
    print(logo)
    first_choice = random.choice(data)
    should_continue = True
    score = 0
    while should_continue:
        second_choice = random.choice(data)
        while first_choice == second_choice:
            second_choice = random.choice(data)
        print(f"Choice A : {first_choice['name']}, {first_choice['description']}, {first_choice['country']}")
        print(vs)
        print(f"Choice B : {second_choice['name']}, {second_choice['description']}, {second_choice['country']}")
        user_choice = input("Select Choice 'A' or Choice 'B'").lower()
        followers_of_a = first_choice['follower_count']
        followers_of_b = second_choice['follower_count']
        result = compare(followers_of_a, followers_of_b)
        if result == user_choice:
            score += 1
            first_choice = second_choice
            print(f"current score = {score}")
        else:
            print("You lost")
            print(f"Final Score : {score}")
            should_continue = False

game()

