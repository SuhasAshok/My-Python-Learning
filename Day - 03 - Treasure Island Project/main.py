print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'ve reached a dead end. Do you want to go "left" or "right". ').lower()
if choice1 == "left":
    choice2= input('Infront of you there is a lake and there is an island in the middle. '
                   'Do you want to "wait" for a boat or "swim" across the lake. ').lower()
    if choice2 == "wait":
        choice3 = input('There are three doors in front of you. '
                        'One is "red" one is "yellow" another is "blue". Choose a door. ').lower()
        if choice3 == "red":
            print("You have been trapped in a room full of Lava. Game Over...")
        elif choice3 == "yellow":
            print("You have been attacked and killed by Red Haired Shanks. Game Over...")
        elif choice3 == "blue":
            print("You have found One Piece and you have the power to take over the entire WORLD."
                  " You've WON the game...")
        else:
            print("You've entered an invalid option. Game Over...")
    else:
        print("You've been devoured by a Giant Squid. Game Over...")

else:
    print("You are attacked by Wild Monsters and got killed. Game Over...")
