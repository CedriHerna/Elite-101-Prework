# I would like my project to represent the logistical front of a store.

print("Welcome to the Perico Logistics ChatBot!")
name = input("What is your name?\n")
age = input("Hello " + name + ", how old are you?\n")

# /*
# The lines above are the basic greetings asking for both a name and age.
# I would like to make it more professional in the future
# */

# I need to first greet the user then output a LIST of option for the user to choose from. 
# Becuase I need to output an list, I will be using an array to easily output the OPTION
# Option must be a variable that is tracked and used to redirect the user. 

print("\nHow can I help you? Type the number of option below\n")


# Where is my package should check the status of the item. Where it is, when it will be arriving, etc.
# 2. Should give simply just the price and probably a break down of the cost.
# 3. Should have responses to fill in to create a shipment. These responses should be a listing of what is being shipped, where it goes, and who gets it.
# 4. Should return the package IDs of all packages in shipment
# 5. This exit should give an option to give feedback to the ChatBot and the services it provides.(Is it possible to hold the feedback so I can see it?)

# These are blank variables that will be filled later on with a proper dictionary




def user_home():
    dictionary_location = "Austin, Tx"
    dictionary_date_of_arrival = "11/11/2024"
    
    array_options = ["1. Where is my package?", "2. What is the price of a certain item?", "3. Create a ticket", "4. List of package IDs", "5. Exit the ChatBot"]


    for option in array_options:
        print(option)

    choice = input("\n")

    if(choice == "1"):
    # Pull from a dictionary where package has estimated time of delievery and where it currently is
        print("What is your package ID?")
        print("Your package is at " + dictionary_location + ". It will arrive " + dictionary_date_of_arrival)
    elif(choice == "2"):
        # Pull from the total cost of a certain delievery and run a calculation (probably in a method) to get the price breakdown.
        print("What is your package ID?")
        print("Your price breakdown is...")
    elif(choice == "3"):
        # These responses should be a listing of what is being shipped, where it goes, and who gets it. It should also create a random package ID in the end.
        shipment = input("What are you shipping?")
        end_location = input("Where will this shipment end up?")
        recipient = input("Who will be recieving this shipment?")
        print("Your created package ID is ...")
    elif(choice == "4"):
        # Should return the package IDs, loaction, total price, and addresses of the shipment.
        print("Return the dictionary in a formated manner")

    elif(choice == "5"):
        print("Have a great day, " + name + "!")
    else:
        print("Return a valid response (Just the number at the start of each option. Eg. \"1\")")



user_home()




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


