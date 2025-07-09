#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D
import random

print("Snake Water Gun Game")
while(True):
    print("Press 1 for Snake")
    print("Press 2 for Water")
    print("Press 3 for Gun")
    print("Press 4 for Exit")
    
    computer = random.randint(1, 3)

    player = int(input("Enter Choice for snake press1, water press2, gun press3: "))
    
    if(computer == player):
        if(computer == 1):
            print("Your choice snake is correct")
        elif(computer == 2):
            print("Your choice water is correct")
        elif(computer == 3):
            print("Your choice gun is correct")
        else:
            print("Invalid choice!")
    elif(player == 4):
        print("Exit!")
        break
    else:
        print("Invalid choice!")
        
    
            
    