# This program is going to be the user playing against the computer that randomly chooses between rock, paper, or scissors.
# First the computer and user must choose an option, then it must be compared to see who wins.
# For the robot to randomly choose an option, I will have to import random.

# Finally, the program must print either win, lose, or tie.

import random
user_choice = input("Choose rock, paper, or scissors.  ").lower() # I have .lower() to make sure that the user can put a upper and lowercase



while(True):

    if(user_choice == "rock" or user_choice == "paper" or user_choice == "scissors"):
        break
    user_choice = input("Please enter the full name. Rock, Paper, or Scissors  ").lower() # I have .lower() to make sure that the user can put a upper and lowercase

# This randomly selects a number 0-2 
computer_choice = random.randint(0,2)
# I assigned a choice depending on which random number the computer selects.
if(computer_choice == 0):
    computer_choice = "rock"
elif(computer_choice == 1):
    computer_choice = "paper"
elif(computer_choice == 2):
    computer_choice = "scissors"



# By using f strings, I don't have to retype the whole word.
# This allows to me return a tie game, as you tie in RPS when you have the same choice

if(computer_choice == user_choice):
    print(f"You chose {user_choice}, and the computer chose {computer_choice}. Tie match!")
    # The if statements below compare the choices and determine the winner by this comparison.
elif(computer_choice == "rock"):

    if(user_choice == "paper"):
        print(f"You chose {user_choice}, and the computer chose {computer_choice}. You Win!")

    elif(user_choice == "scisors"):
        print(f"You chose {user_choice}, and the computer chose {computer_choice}. Computer Wins!")

elif(computer_choice == "paper"):

    if(user_choice == "scissors"):
        print(f"You chose {user_choice}, and the computer chose {computer_choice}. You Win!")

    elif(user_choice == "rock"):
        print(f"You chose {user_choice}, and the computer chose {computer_choice}. Computer Wins!")

elif(computer_choice == "scissors"):

    if(user_choice == "rock"):
        print(f"You chose {user_choice}, and the computer chose {computer_choice}. You Win!")

    elif(user_choice == "paper"):
        print(f"You chose {user_choice}, and the computer chose {computer_choice}. Computer Wins!")

# The code seems to work  well, but I don't think the comparisons are written well. I am not sure if there is function that can compare them better so I would need to do research to decrease the chain of if statements.
# I could also have an emcompassing while loop that will allow the user to continue playing until they type the word quit.
