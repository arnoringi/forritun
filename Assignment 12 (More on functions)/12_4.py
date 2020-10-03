def is_valid(input_list):
    try:
        for digit in input_list:
            int(digit)
        check = int(input("Consecutive check: "))
        return check
    except ValueError:
        return None

def consecutive_check(check, input_list):
    value = False

    previous_int = 0
    current_int = 0

    for num in input_list:
        current_int = int(num)
        if current_int == previous_int and current_int == check:
            value = True
            break
        previous_int = current_int
    return value

# Main program starts here
input_list = input("Enter elements of list separated by commas: ").strip().split(',')
check = is_valid(input_list)

if check == None:
    print("Error: enter only integers.")
else:
    value = consecutive_check(check, input_list)
    print(value)