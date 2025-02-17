# I have to create a function that takes in a sentance and then returns the longest word within the sentance.
# I will be using the split function to break the sentance into words then removing 1 from the length if there is punctuation.

# First I create the input:
sentence = input("Please enter your sentance.")

# I am  creating an array that holds the lengths of each word in the sentance so I can compare them later on.
arrayLengths = []



# Here I define the function
def longest_word(string):

    # I split each word apart from the main sentence the user gives.
    split_sentence = string.split(" ")

    for word in split_sentence:
        # I find if there is any punctuation and subtract one since there will conly be a punctuation mark at the end.
        if(word.find("!") != -1):
            arrayLengths.append(len(word) -1)
            
        elif(word.find(".") != -1):
            arrayLengths.append(len(word) - 1)
            
        elif(word.find("?") != -1):
            arrayLengths.append(len(word) - 1)
            
        else:
            arrayLengths.append(len(word))

    # These two variables will help deduce which words are the largest.
    largest_size = 0
    position = 0
    for i, size in enumerate(arrayLengths):
        # I am itterating through each word to find which one is the longest, by storing the size of the longest word I find as I am itterating and comparing it to the next size in the array.
        # By using enumerate, I get to store the position of the largest word.
        if(i == 0):
            largest_size = size
        
        if(largest_size < size):
            position = i
            largest_size = size
    
    # Finally I print the word out by using the position of the longest and the split sentence array which holds all the words.
    print(split_sentence[position])

# Now I call the function.
longest_word(sentence)

# I ran out of time so I wasn't able to tackle if there are two words that are the longest, but I would have to store the postion of both of them and then return a print statement that tells the user there are two words while printing both of them.

