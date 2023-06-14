marks = int(input("Enter The Mark: "))

if(marks>= 80):
    print('The Grade is: A+')
    
elif (marks>= 70 and marks<80 ):
    print('The Grade is: A')
    
elif (marks>= 60 and marks<70 ):
    print('The Grade is: A-')
    
elif (marks>= 50 and marks<60 ):
    print('The Grade is: B')
    
elif (marks>= 40 and marks<50 ):
    print('The Grade is: C')
    
elif (marks>= 33 and marks<40 ):
    print('The Grade is: D')
    
else:
    print(" F ")
    