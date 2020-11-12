QUIT = 'q'              # Input to exit program
LENGTH = 13             # Number of digits + seperators
SEPERATOR = '-'         # What seperates the number
POSITIONS = [1, 5, 11]  # Where the dashes are located

def enter_isbn():
    ''' ISBN input '''
    isbn = input("Enter an ISBN: ")
    return isbn

def check_valid(isbn):
    ''' Checks all conditions for isbn number '''
    valid = []

    seperator = check_seperator(isbn)
    valid.append(seperator)
    integer = check_int(isbn)
    valid.append(integer)
    length = check_len(isbn)
    valid.append(length)

    for value in valid:
        if value != True:
            return False
    return True

def check_seperator(isbn):
    ''' Checks if SEPERATOR is in correct place '''
    index = 0

    for digit in isbn.strip():
        for position in POSITIONS:
            if index == position:
                if digit != SEPERATOR:
                    return False
        index += 1
    return True

def check_int(isbn):
    ''' Checks if correct digits are integers '''
    temp_list = POSITIONS
    index = 0

    for digit in isbn.strip():
        for position in temp_list:
            if index == position:
                temp_list = temp_list[1:] # Remove first digit in temp_list
                break # Skip rest of for-loop
            else:
                try:
                    digit = int(digit)
                    break # To prevent repetition
                except ValueError:
                    return False
        index += 1
    return True

def check_len(isbn):
    ''' Checks if ISBN number is correct length '''
    if len(isbn) == LENGTH:
        return True

def print_outcome(valid):
    ''' Prints outcome '''
    if valid:
        print("Valid format!")
    else:
        print("Invalid format!")    

# Main program starts here
isbn = enter_isbn()

while isbn != QUIT:
    valid = check_valid(isbn)
    print_outcome(valid)
    isbn = enter_isbn()