import random 

options = ("rock", "paper", "scissor")
player = None 
computer = random.choice(options)

print()
while player not in options:
    player = input("Choose one (rock,paper,scissor): ")
print(f"Player : {player}")
print(f"Computer : {computer}")    
if player == computer:
    print("Tie")
elif player == "scissor" and computer == "paper":
    print("Player wins!")

elif player == "paper" and computer == "rock":
    print("Player wins!")

elif player == "rock" and computer == "scissor":
    print("Player wins!")
else :
    print("Computer wins!")