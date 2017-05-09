##################
## CS50 PSET 6 - mario.py (more comfortable)
## Mario.py prints out a double half-pyramid of a specified height
##################

height = int(input("Height:"))

hash1 = 0
line = 1
hash2 = 0

if (height > 0 and height < 23):
    
    for line in range (height):
        
        space = height-line
        for space in range(1, space):
            print(" ", end="")
            space-=1
        
        for hash1 in range (hash1+1):
            print("#", end="")
            hash1+=1
        
        print("  ", end="")
        
        for hash2 in range (hash2+1):
            print("#", end="")
            hash2+=1
        
        line+=1
        print("\n", end="")

else:
    print("Improper height")
