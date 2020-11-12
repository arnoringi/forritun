def options():
    """ Prints options for user to choose from """
    print("1: Compute the sum of 1..n")
    print("2: Compute the product of 1..n")
    print("9: Quit")
    try:
        option = int(input("Choice: "))
    except:
        return None
    return option
    
def is_valid(option):
    """ Checks input from user """
    if option == 1:
        sum_of_n()
    elif option == 2:
        product_of_n()
    elif option == 9:
        return 9
    else:
        return None

def sum_of_n():
    """ Calculates the sum from 1 up to n """
    try:
        input_value = int(input("Enter value for n: "))
    except:
        return None
    
    sum_int = 0

    try:
        for number in range(1, input_value+1): # Positive numbers
            sum_int += number
        
        print("The result is:", sum_int)
        return None
    except:
        return None

def product_of_n():
    """ Calculates the product from 1 up to n """
    try:
        input_value = int(input("Enter value for n: "))
    except:
        return None
    
    sum_int = 1
    
    try:
        for number in range(1, input_value+1):
            sum_int *= number
        
        print("The result is:", sum_int)
        return None
    except:
        return None

# Main program starts here
while True:
    input_value = options()
    valid = is_valid(input_value)

    if valid == 9:
        break
    else:
        continue