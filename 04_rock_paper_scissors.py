# Official Game Website : https://wrpsa.com/the-official-rules-of-rock-paper-scissors/

# Import random module 
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameOptions = [rock, paper, scissors]

playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if playerChoice >= 3 or playerChoice < 0:
    print("Invalid number. You lose!")
else:
    print(gameOptions[playerChoice])
print(gameOptions[playerChoice])

computerChoice = random.randint(0,2)
print("Computer chose: ")
print(gameOptions[computerChoice])
    
if playerChoice == 0 and computerChoice == 2:
    print("You Win!")
elif computerChoice == 0 and playerChoice == 2:
    print("You Lose!")
elif playerChoice > computerChoice:
    print("You Win!")
elif computerChoice > playerChoice:
    print("You Lose!")
elif computerChoice == playerChoice:
    print("You draw!")
