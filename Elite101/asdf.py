def odd(min, max):
    number = min
    if(min % 2 == 0):
        number += 1

    odd_list = []
    while number <= max:
        odd_list.append(number)
        number+= 2
    return odd_list
    
print(odd(1,13))