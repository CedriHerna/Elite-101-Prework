
# Testing String
# counter = 0
test_string = "caps"
# 0, 3

# Array index
array_indexes = []

# Function:
def capital_indexes(string):
    for i, charater in enumerate(string):

        if(charater.isupper()):

            array_indexes.append(i)
            # counter++
    # if there are no appends{
    return array_indexes

    
print(capital_indexes(test_string))



# For{
# Every charater in the string

# if(Is capitalized):
# enumerate
# }
# Return array

# print(Function)


