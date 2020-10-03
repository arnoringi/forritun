import math

def input_desc():
    """ Prints input description """
    # Print is set up in this way because having it in one line would be too long
    print("Please choose one of the options below:")
    print("a. Display the sum of the first N natural numbers.")
    print("b. Display the sum of the first N Fibonacci numbers.")
    print("c. Display the approximate value of e using N terms.")
    print("x. Exit from the program.")
    return input_func()

def input_func():
    """ Returns input information """
    input_str = input("\nEnter option: ").lower()

    # Input information
    if input_str == 'a':
        return sum_natural()
    elif input_str == 'b':
        return sum_fibonacci()
    elif input_str == 'c':
        return approximate_euler()
    elif input_str == 'x':
        return
    else:
        print("Unrecognized option", input_str)
        return input_desc()

# Option A
def sum_natural():
    """ Returns the sum of the first n numbers """
    input_int = input("Enter N: ")

    if input_int.isdigit():
        input_int = int(input_int)
        if input_int >= 2:
            sum_int = 0

            # For loop that adds onto sum_int n number of times
            for add_on in range(1, input_int+1):
                sum_int += add_on
            
            print("Natural number sum:", sum_int)
        else:
            print("Error:", input_int, "was not a valid number.")
    else:
        print("Error:", input_int, "was not a valid number.")
    return input_func()

# Option B    
def sum_fibonacci():
    """ Returns the sum of the first n Fibonacci numbers """
    input_int = input("Enter N: ")

    if input_int.isdigit():
        input_int = int(input_int)
        if input_int >= 2:
            # These variables are meant for the start of the sequence
            num1 = 0
            num2 = 1

            # sum_int is the sum of num1 and num2, sum_total is the sum of the entire sequence
            sum_int = 0
            sum_total = 1

            # The for loop adds the most recent numbers (num1, num2) together, then changes them
            for count in range(2, input_int):
                sum_int = num1 + num2
                num1 = num2
                num2 = sum_int
                sum_total += sum_int
            
            print("Fibonacci sum:", sum_total)
        else:
            print("Error:", input_int, "was not a valid number.")
    else:
        print("Error:", input_int, "was not a valid number.")
    return input_func()

# Option C
def approximate_euler():
    """ Returns the approximation of the Euler number 
    (the number e that is the base of the natural logarithm) 
    using the first n terms in the series below """
    input_int = input("Enter N: ")

    if input_int.isdigit():
        input_int = int(input_int)
        if input_int >= 2:
            sum_int = 1

            # The for loop adds 1 divided by the factorial of num, input_int times
            for num in range(1, input_int):
                sum_int += 1/math.factorial(num)
            
            print("Euler approximation:", round(sum_int, 5))
        else:
            print("Error:", input_int, "was not a valid number.")
    else:
        print("Error:", input_int, "was not a valid number.")
    return input_func()

#To start the program
input_desc()

### COMMENT
# Er ekki alveg að fatta hvernig það á að skila None. Held ég gæti það ef að ég væri ekki með
# input_desc() og input_func() sem föll. En veit ekki hvernig ég fer að þessu ef ég vill bara að
# input_desc birtist einu sinni í byrjun, svo bara input_fun(). Datt í hug while lykkju (while != x),
# en það var ekki alveg að ganga. Þessi kóði virkar samt.
# Væri til í að fá feedback um þetta. :)