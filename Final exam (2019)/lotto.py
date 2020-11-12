LENGTH = 5
LOW = 1
HIGH = 40

def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        return None

def check_valid(lotto_num):
    ''' Checks if lotto numbers are valid '''
    integers = check_integers(lotto_num)
    if integers:
        length = check_length(lotto_num)
        if length:
            is_range = check_range(lotto_num)
            if is_range: # All criteria fufilled
                return True
    return False

def check_integers(lotto_num):
    ''' Checks if all digits are integers '''
    for digit in lotto_num:
        try:
            digit = int(digit)
        except ValueError:
            return False
    return True

def check_length(lotto_num):
    ''' Checks length of input '''
    if len(lotto_num) == LENGTH:
        return True
    else:
        return False

def check_range(lotto_num):
    ''' Checks if all digits are within range '''
    lotto_num = list(lotto_num)
    lotto_num = [int(num) for num in lotto_num]

    for digit in lotto_num:
        if digit >= LOW and digit <= HIGH:
            continue
        else:
            return False
    return True

def create_list(file_object):
    ''' Creates a list of lotto numbers from file '''
    winning_list = []
    
    for line in file_object:
        for number in line.strip().split():
            winning_list.append(int(number))
        winning_list.append("\n")
    return winning_list

def check_list(lotto_num, winning_list):
    ''' Checks if numbers are in winning list '''
    lotto_num = [int(num) for num in lotto_num]
    index = 0

    for number in lotto_num:
        for winning_number in winning_list:
            if number == winning_number: # If match
                winning_list[index] = str(winning_number) + '*'
            index += 1
        index = 0 # Index reset
    return winning_list

def print_result(result):
    ''' Prints out result of which numbers had a match '''
    temp_list = []
    print_list = []

    for digit in result:
        if digit == '\n':
            temp_list = [str(num) for num in temp_list]
            print_list.append(" ".join(temp_list))
            temp_list.clear()
        else:
            temp_list.append(digit)
    print("\n".join(print_list))

# Main program starts here
file_name = input("Enter file name: ").strip().lower()
file_object = open_file(file_name)

if file_object == None:
    print("File {} not found!".format(file_name))
    pass
else:
    lotto_num = input("Enter winning numbers: ").strip().split()
    valid = check_valid(lotto_num)
    if valid:
        winning_list = create_list(file_object)
        result = check_list(lotto_num, winning_list)
        print_result(result)
    else:
        print("Winning numbers are invalid!")