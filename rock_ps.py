# Rock, Paper, Scissors Game 

# rps = "rock, paper, scissors"
# ask user rps?
# put rps into a list and generate a random item in the list
# print item
# validate rps rules 

# make game start again if user inputs anything except rock, paper, scissors 
# make game start again after it has ended
# when user ends game print "END GAME"

import random


print("************ Rock, Paper, Scissors Game **************")
print("")

rps = input("Rock, Paper, Scissors?... \n")

# if rps.lower() != "rock" or "paper" or "scissors":
#  print("Please enter a valid input")

rps_options = ["rock", "paper", "scissors"]
comp_choice = random.choice(rps_options)

print("")

print("***************************")
print("- You chose: " + rps.capitalize() )
print("- The Computer chose: " + comp_choice.capitalize() )
print("***************************")

print("")

if rps.lower() == comp_choice:
 print("The Game Is A Draw")

if rps.lower() == "rock" and comp_choice == "scissors":
 print("You Win!!")

if rps.lower() == "scissors" and comp_choice == "rock":
 print("The Computer Wins LOL")


if rps.lower() == "paper" and comp_choice == "rock":
 print("You Win!!")

if rps.lower() == "rock" and comp_choice == "paper":
 print("The Computer Wins LOL")


if rps.lower() == "scissors" and comp_choice == "paper":
 print("You Win!!")

if rps.lower() == "paper" and comp_choice == "scissors":
 print("The Computer Wins LOL")


print("")
print("********************** End Game ***********************")


