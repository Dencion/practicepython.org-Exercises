#Exercise 8
#Make a two-player Rock-Paper-Scissors game.
#(Hint: Ask for player plays (using input), 
#compare them, print out a message of congratulations to the winner,
#and ask if the players want to start a new game)

#Functions
def compare(play1, play2):
    if play1 == play2:
        return("It's a tie!")
    elif play1 == 'rock':
        if play2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif play1 == 'scissors':
        if play2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif play1 == 'paper':
        if play2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
       

print("Welcome to Rock-Paper-Scissors!")
print("1-rock\n"+"2-scissors\n"+"3-paper")
gameStatus = ''

while gameStatus != 'n':
    play1 = input("Player one pick your play:")
    play2 = input("Player two pick your play:")

    print(compare(play1,play2))
    gameStatus = input("Would you like to play another game y/n ?")
