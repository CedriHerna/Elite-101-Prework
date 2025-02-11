# In this coding task we have to return the indexes of Captial letters in a string

string = "WasSup"
store_index = []

def capital_indexes(string):

    for i, charater in enumerate(string):
        
        if(charater.isupper()):
            store_index.append(i)
    return store_index

print(capital_indexes(string))












