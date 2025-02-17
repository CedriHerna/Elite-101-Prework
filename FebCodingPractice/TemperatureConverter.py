# This project is about converting one unit of measurement into another. I need to be weary of them not entering a supported temperature.

# I ask first what unit of measurement they want to convert from while making sure it is a supported unit.
type1 = input("Which scale are you converting from? Please enter F for Fahrenheit, C for Celsius, and K for Kelvin ").upper()


while(True):
    if(type1 == "C" or type1 == "F" or type1 == "K"):
        break
    type1 = input("Please only enter the first letter.")

type2 = input("Which scale are you converting to? ")

while(type2 == type1):

    while(True):
        if(type1 == "C" or type1 == "F" or type1 == "K"):
            break
        type2 = input("Please only enter the first letter that isn't the same as your starting scale.")

# This asks for the temperature and converts it into a float since it gets multiplied by floats
temp = float(input("Please enter your starting temperature"))

# We need conversion factors to ensure we are quickly converting our values:
# I am going to name them the capitalized first letter of the scale I am converting from and the first letter I am converting to.
CF = temp * (9/5) + 32
CK = temp + 273.15

FC =  (temp - 32) * (5/9)
FK =  FC + 273.15

KC = temp - 273.15
KF = KC * (9/5) + 32


if(type1 == "C"):

    if(type2 == "F"):
        print(CF)
        
    elif(type2 == "K"):
        print(CK)

elif(type1 == "F"):

    if(type2 == "C"):
        print(FC)

    elif(type2 == "K"):
        print(FK)

elif(type1 == "K"):

    if(type2 == "C"):
        print(KC)
    
    elif(type2 == "F"):
        print(KF)


# This project could be improved by not using so many if statements and instead using some sort of comparing feature between the users inputs and which comparing factor to use.
# It could also be improved in it's comparing logic for edge cases to decrease runtime.