##################
## CS50 PSET 6 - greedy.py 
## greedy.py calculates the minimum number of coins required to give a user change.
##################

change = int(input("O hai, how much change is owed: "))
cents = int(change*100)
leftover = cents
count = 0

if (change > 0):
    
    i = 0 
    # counting the quarters 25cents
    for i in range (cents//25):
        leftover = leftover - 25
        count +=1
        
    i = 0 
    # counting the dimes 10cents
    for i in range (leftover//10):
        leftover = leftover - 10
        count +=1

    i = 0 
    for i in range (leftover//5):
        leftover = leftover - 5
        count +=1

    i = 0 
    for i in range (leftover//1):
        leftover = leftover - 1
        count+=1

    print ("You will have",count, "coins")


else: 
    print("No negative values.")
