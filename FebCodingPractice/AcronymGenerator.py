# This project is about finding the first letter in each word and adding all the letters together in one output which has each letter capitalized while ignoring the words "or" and "and".
# I need to be weary of accidental user inputs and create edge cases that allow the code to work no matter what the user inputs.


# First I take in a sentance or phrase and define a string that will hold the acronym
acronym = ""
phrase = input("Enter a phrase or sentance  ")
# Just in case the user enters in something blank, I have it return No Acronym
while(len(phrase) == 0 or phrase[0] == " "):
    if(len(phrase) == 0):
        print("No Acronym")
        break
    else:
        # In case the user puts in a space in the beginning, I ask them to try entering it again.
        phrase = input("Please input your phrase or sentance without a space at the start  ")

# Since the phrase/Sentance is going to start with a letter, I store the first letter in what is going to be the Acronym 
if(len(phrase) > 0):
    acronym = phrase[0]

    # Next I make an array that will store the index of each space, which I can then use to track the first letter of each word.
    array_of_indexes = []

    # In this for loop I am finding every space and adding it's index in my array.
    for i, char in enumerate(phrase):
        
        if(char == " "):
            array_of_indexes.append(i)

    # Here I check whether or not two spaces are surrounding the words "or" or "and"
    for i in array_of_indexes:

        for j in array_of_indexes:

            if(phrase[i+1:j] == "and"):
                array_of_indexes.remove(i)

            if(phrase[i+1:j] == "or"):
                array_of_indexes.remove(i)

            

    # I then use the index values to find the first letter of each word.
    for i in array_of_indexes:

        # My if statement takes into account that someone could've accidentally put a space at the end.
        if(i < len(phrase) - 1):
            acronym += phrase[i+1]

    # Finally I uppercase all of the first letters and print it to the console.


    print(acronym.upper())

# This could be improved by finding a better method of search and integrating both for loops into one.
# Furthermore, my code doesn't take into account that a user can input two spaces instead of one. By considering this, the run time could be decreased. I would have to program a way to see if two space indexes are right next to each other and then remove the first space index of the two.













