
#Exercise 9 
#Generate a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, then tell them whether they guessed too low,
#too high, or exactly right. (Hint: remember to use the user input 
#lessons from the very first exercise)
#Extras:
#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, 
#and when the game ends, print this out.
import random


userNum = 0
randNum = random.randint(1, 9)
count = 0

while userNum != randNum:
    
    count += 1
    userNum = int(input("Pick a number between 1 and 9:"))
    
    if userNum == randNum:
        print("Congrats You got it!")
    elif userNum < randNum:
        print("Number too low,go higher:")
    else:
        print("Number too high,go lower:")
        
print("Total amount of guesses:",count)   
