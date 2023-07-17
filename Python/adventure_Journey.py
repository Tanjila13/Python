name = input("Enter your name: ")
print("Welcome",name,"this is an advanture")

choose = input("You're on a road.It has come to an end And you can go left or right.Which way you would like to go? ").lower()


if choose == "left":
    choose = input("You come to a river! You can swim or walk around it?")
    
    if choose == "swim":
        print("You swam and were eaten by alligator!You lose!")
        
    elif choose == "walk":
        print("You walked many miles, ran out of water!")
        
    else:
        print("Not a valid option! You lose!")
          
    
elif choose == "right":
    choose = input("You come to a bridge.Do you want to cross it or want to go back?")
    
    if choose == "back":
        print("You go back and lose")
    
    elif choose == "cross":
        choose = input("You cross the bridge and get a gold bar.Do you want to teke (Yes/No)?")
        
        if choose == "yes":
            print("You got a gold bar! You won!")
            
        elif choose == "no":
            print("You lose the game!")
        
        else:
            print("Not a valid option! You lose!")
               
        
    else:
      print("Not a valid option! You lose!")   
    
else:
    print("Not a valid option! You lose!")
    

print("Thank You",name)
