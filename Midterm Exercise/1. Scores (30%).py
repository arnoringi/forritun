def is_valid(number_list):
    """ Checks if number list is equal or more than 2 """
    if len(number_list) >= 2:
        return number_list
    else:
        return None

def calculate_scores(number_list_valid):
    """ Calculates sum of list, without lowest 2 digits """
    number_list = []

    for digit in number_list_valid: # Changing all digits to float
        digit = float(digit)
        number_list.append(digit)
    
    for i in range(2): # Removing lowest 2
        number_list.remove(min(number_list))
    
    sum_float = 0
    for digit in number_list: # Adding digits to sum
        sum_float += digit
    
    print("Sum of scores (two lowest removed):", sum_float)

### Main program starts here
number_list = input("Enter scores separated by space: ").split(' ')
number_list_valid = is_valid(number_list)

if number_list_valid == None:
    print("At least two scores needed!")
else:
    calculate_scores(number_list_valid)