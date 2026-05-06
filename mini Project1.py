#guess the number 


import random


target = random.randint(1,100)

while True:
    userChoice = int(input("guess the target : "))
    if(userChoice == target):
        print("success : correct Guess !!")
        break
    elif(userChoice < target ):
        print("take big num")
    else:
        print("take small guess")



print("game over")



