# Lesson 8 Section 1.3
a_string = "4Letter"
def contains_digits(a_string):

    for character in a_string:

        if(character.isdigit()):
            return True
        
    return False

print(contains_digits(a_string))
        