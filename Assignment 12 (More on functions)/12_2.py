def remove_evens(int_list):
    """ Removes even integers from int_list, thus modifying int_list """
    even_int = []

    # Even digit checker
    for digit in int_list:
        if digit % 2 == 0:
            even_int.append(digit)
    
    # Even digit remover
    for digit in even_int:
        int_list.remove(digit)

def remove_evens2(int_list):
    """ Returns a new list with only odd integers from int_list, without modifying int_list """
    new_list = []

    for digit in int_list:
        if digit % 2 == 1:
            new_list.append(digit)
    
    return new_list

# Main starts here
a_list = [1,2,2,3,4,5]
print(a_list)
remove_evens(a_list)
print(a_list)
    
b_list = [1,2,3,4,4,5,6,7,8,9,10]
c_list = remove_evens2(b_list)
print(b_list)
print(c_list)