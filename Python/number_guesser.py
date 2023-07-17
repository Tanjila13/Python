import random

top_range = input("Type any number: ")

if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range <= 0:
        print("please type a number large than 0")
        quit()
        
else:
    print('Please type a Number')
    

random_number = random.randint(0, top_range)
guess = 0


while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
    else:
        print("Please type any number next time ") 
        continue
      
    if user_guess == random_number:
        print("YES!! You got it")
        break
        
    elif user_guess > random_number:
            print("You were above the number!")
            
    else:
            print("You were below the number!")
            
       
        
print("You got it",guess,"guesses  ")