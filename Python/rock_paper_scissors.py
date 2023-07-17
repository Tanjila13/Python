import random

user_win = 0
computer_win = 0

Choose = ["rock","paper","scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Quit: ").lower()
    if user_input == "quit": 
        break
        

    if user_input not in Choose:
        continue

    random_number = random.randint(0,2)
    #rock = 0, paper = 1, sissors = 2

    computer_choose = Choose[random_number]
    print("Computer Picked",computer_choose + ".")


    if user_input == "rock" and computer_choose == "scissors":
        print("You Won!")
        user_win += 1


    elif user_input == "paper" and computer_choose == "rock":
        print ("You Won!")
        user_win += 1
    
    
    elif user_input == "scissors" and computer_choose == "paper":
        print("You Won!")
        user_win += 1
    
    else:
        print("You lost!:(")
        computer_win += 1
        
        
print("You Won",user_win,"times!")
print("Computer Won",computer_win,"times!")

print("Goodbye")