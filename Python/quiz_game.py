print("Welcome to my computer quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("okey! Let's play :)")
score = 0
    


ans = input("what's my favorite colour ?")
if ans.lower() == "blue":
    print('correct')
    score +=1

else:
    print('Incorrect') 
    
     

ans = input("what's my favorite fruit?")
if ans.lower() == "litchi":
    print('correct')
    score +=1 

else:
    print('Incorrect') 
  
    
    
ans = input("what's my favorite flower?")
if ans.lower() == "rose":
    print('correct')
    score+=1
else:
    print('Incorrect') 
    
    
    
ans = input("what's my favorite food?")
if ans.lower() == "burger":
    print('correct')
    score+=1

else:
    print('Incorrect') 
    
    
print("you got score = "+str(score))
print("you got = "+str((score /4)* 100) + "%")
 