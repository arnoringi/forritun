#list_to_int_tuple function goes here
def list_to_int_tuple(a_list):
    tuple_list = []

    for digit in a_list:
        try:
            int_digit = int(digit)
            tuple_list.append(int_digit)
        except ValueError:
            pass
    
    return tuple(tuple_list)
    
# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_int_tuple(a_list)
print(a_tuple)