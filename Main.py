import random
# My project is going to be a chatbot that has to help a customer return or exhange an item

# This is an array that has the list of clothing items
clothing_list = ["Shirt", "Shirt", "Skirt", "Pants", "Dress"]

# This is going to randomize a number and then randomly give the user an item.
 
# random reciept number generator
random_reciept_num = random.randint(1, 100)
# random clothing item
random_item = random.choice(clothing_list)

print("This is an example recipt you will have.")



print("Welcome to the Perico's Clothing ChatBot!")
name = input("What is your name?\n")
age = input(f"Hello {name}, how old are you?\n")

# hello
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
array_options = ["1. Help me return my item.", "2. Help me exhange my item.", "3. Exit the chatbot."]

def user_clothing():
    
    print("What sort of clothing do you have? Is it a shirt, short, skirt, dress, or hoodie?")
    


def user_choice():
    
    for option in array_options:
        print(option)

    choice = input("\n")

    
    if(choice == "1"):
        reciept = input("Please enter ")
    elif(choice == "3"):
        print("Have a great day, " + name + "!")
    else:
        print("Return a valid response (Just the number at the start of each option. Eg. \"1\")")



user_choice()




# for option in array_options:
#     print(option)

# choice = input("\n")

# if choice == 1,2,3,4

# if(choice == "1"):
#     # Pull from a dictionary where package has estimated time of delievery and where it currently is
#     print("What is your package ID?")
#     print("Your package is at " + dictionary_location + ". It will arrive " + dictionary_date_of_arrival)

# elif(choice == "2"):
#     # Pull from the total cost of a certain delievery and run a calculation (probably in a method) to get the price breakdown.
#     print("What is your package ID?")
#     print("Your price breakdown is...")

# elif(choice == "3"):
#     # These responses should be a listing of what is being shipped, where it goes, and who gets it. It should also create a random package ID in the end.
#     shipment = input("What are you shipping?")
#     end_location = input("Where will this shipment end up?")
#     recipient = input("Who will be recieving this shipment?")
#     print("Your created package ID is ...")

# elif(choice == "4"):
# 	# Should return the package IDs, loaction, total price, and addresses of the shipment.
#     print("Return the dictionary in a formated manner")

# elif(choice == "5"):
#     print("Have a great day, " + name + "!")
# else:
#     print("Return a valid response (Just the number at the start of each option. Eg. \"1\")")


