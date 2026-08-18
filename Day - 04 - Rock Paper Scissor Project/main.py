import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
user_choice = int(input("Choose any one option: 0 for Rock, 1 for Paper, 2 for Scissors: "))
if user_choice >= 0 and user_choice < 3:
    print(f"You chose{game[user_choice]}")

computer_chose = random.randint(0,2)
print("Computer chose:")
print(game[computer_chose])


if user_choice >= 3 or user_choice < 0:
    print("You have entered an invalid option ")
elif computer_chose == 0 and user_choice == 2:
    print("You lose")
elif computer_chose == 2 and user_choice == 0:
    print("You win")
elif computer_chose == user_choice:
    print("Draw")
elif computer_chose > user_choice:
    print("You lose")
elif computer_chose < user_choice:
    print("You win")