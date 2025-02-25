import random
# My project is going to be a chatbot that has to help a customer return or exhange an item

# This is an array that has the list of clothing items
clothing_list = ["Shirt", "Shirt", "Skirt", "Pants", "Dress"]

# To return an item, the user needs a list of return locations
return_hubs = ["Austin", "Round Rock", "Pflugerville", "Georgetown", "Cedar Park"]

clothing_dictionary = {"Shirt" : 4.00, "shorts" : 3.25, "Skirt" : 3.25, "Pants" : 4.00, "Dress" : 6.00}

# This is going to randomize a number and then randomly give the user an item.
 
# random reciept number generator
random_reciept_num = random.randint(1, 100)

# random clothing item
random_item = random.choice(clothing_list)

print(f"This is an example recipt you will have. \nReciept Number: {random_reciept_num}\nItem: {random_item}")



print("\n\nWelcome to the Perico's Clothing ChatBot!")
name = input("What is your name?\n")
age = input(f"Hello {name}, how old are you?\n")

# /*
# The lines above are the basic greetings asking for both a name and age.
# */

# I need to first greet the user then output a LIST of options for the user to choose from. 
# Becuase I need to output an list, I will be using an array to easily output the OPTION
# Option must be a variable that is tracked and used to redirect the user. 

print("\nWould you like to return or exhange an item? Type the number of option below\n")


# Here are the options that the user can choose from
# 1. Return - 
# 2. Exchange - 
array_options = ["1. Help me return my item.", "2. Help me exhange my item.", "3. Confirmation/Exchange Number", "4. Exit the chatbot."]




def user_choice():
    
    for option in array_options:
        print(option)

    choice = input("\n")

    
    if(choice == "1"):
        return_item()

    elif(choice == 2):
        print("Fortnite baby")
    elif(choice == 3):
        print("Confirmation and exchange stuffs.")
    elif(choice == "4"):
        print("Have a great day, " + name + "!")
    else:
        print("Return a valid response (Just the number at the start of each option. Eg. \"1\")")


def return_item():
    
    reciept = input("Please enter the reciept number to confirm your purchase. If you chose the wrong option, type exit. ").lower()

    while(True):   #Looping indefinetly so the user can punch in the right code.

        if(reciept == "exit"):
            print("Exiting to home page.")
            return       #Allows me to skip to rest of the code after this while loop and return to the main function.
        elif(int(reciept) == random_reciept_num):
            print(f"Thank you for your confirmation. You are trying to return a {random_item}.")
            break
        else:
            reciept = input("Unknown reciept. Please try again. *Enter the receipt number that is at the very top of the terminal* ")

    print(f"The return value for this item is $ {clothing_dictionary[random_item]}")
    confirmation = input("Do you confirm that you are returning your item for this price? (Yes or No) *Notice: If you type \"No\" you will be sent back to the home page.").lower()
    
    while(True):

        if(confirmation == "yes"):
            break
        elif(confirmation == "no"):
            print("\n\n")
            return
        else:
            confirmation = input("Please reenter your response as either \"Yes\" or \"No\".")
    
    confirmation_number = random.randint(0,10000)
    print(f"Wonderful! Please go to any close Perico Clothing hub and show them this confirmation code at the return desk: {confirmation_number}")
    print("\n\n")


def exchange_item():

    reciept = input("Please enter the reciept number to confirm your purchase. If you chose the wrong option, type exit. ").lower()

    while(True):   #Looping indefinetly so the user can punch in the right code.

        if(reciept == "exit"):
            print("Exiting to home page.")
            return       #Allows me to skip to rest of the code after this while loop and return to the main function.
        elif(int(reciept) == random_reciept_num):
            print(f"Thank you for your confirmation. You are trying to exchange your {random_item} for another item.")
            break
        else:
            reciept = input("Unknown reciept. Please try again. *Enter the receipt number that is at the very top of the terminal* ")

    print("What item would you like to exhange for? You can only exhange for an item less or equal to the return value of your item")

    for i, item in enumerate(clothing_dictionary):

        print(f"{i}, {item}")


user_choice()

