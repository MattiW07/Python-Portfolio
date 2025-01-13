#Matti Wachalski
#Rock Paper Scissors

#Initialize
import random
wins = 0
losses = 0
ties = 0
#Functions
def play_rockpaperscissors():
    global wins
    global ties
    global losses
    print("Welcome to Rock, Paper, Scissors! If you ever want to end the game, type in quit. Good Luck!")
    print("What is your name?")
    b=0
    while b==0:
        player = input("Rock, Paper, Scissors, Go:  ")
        player = player.lower()
        computer = (random.randint(1,3))
        if player == "quit":
            print("Thanks for playing. See you next time!")
            break
        if computer == 1:
            computer = "rock"
            print("The computer's move is rock!")
        if computer == 2:
            computer = "paper"
            print("The computer's move is paper!")
        if computer == 3:
            computer = "scissors"
            print("The computer's move is scissors!")
        if player == "rock" and computer == "rock":
            print("It is a Tie!")
            ties = ties + 1
        if player == "paper" and computer == "paper":
            print("It is a Tie!")
            ties = ties + 1
        if player == "scissors" and computer == "scissors":
            print("It is a Tie!")
            ties = ties + 1
        if player == "rock" and computer == "paper":
            print("You lose!")
            losses = losses + 1
        if player == "rock" and computer == "scissors":
            print("You win!")
            wins = wins + 1
        if player == "paper" and computer == "rock":
            print("You win!")
            wins = wins + 1
        if player == "paper" and computer == "scissors":
            print("You lose!")
            losses = losses + 1
        if player == "scissors" and computer == "rock":
            print("You lose!")
            losses = losses + 1
        if player == "scissors" and computer == "paper":
            print("You win!")
            wins = wins + 1
        print("You have " + str(wins) + " wins, " + str(ties) + " ties, and " + str(losses) + " losses.")




#Main
play_rockpaperscissors()
