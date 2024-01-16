import random

options = ("rock", "paper", "scissors") #fixed data so using a tuple
player = None
computer = random.choice(options) # here computer is a variable which will
                                  # choose the items from the tuple "options"

while player not in options:
    print("INVALID")
    player = input("Enter a choice (Rock, paper, scissors)---->>>>   ")


print(f"Player: {player}")
print(f"Computer: {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("you win!")
elif player == "paper" and computer == "rock":
    print("you win!")
elif player == "scissors" and computer == "paper":
    print("you win!")

else:
    print("you loose")
     