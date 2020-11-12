def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    a_list = [int(i) for i in a_list]
    return a_list

def even_sum(a_list):
    sum_int = 0

    for digit in a_list:
        if digit % 2 == 0:
            sum_int += digit
        else:
            pass
    
    return sum_int

# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))