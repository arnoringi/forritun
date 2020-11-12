def make_set(my_list):
    my_list = [int(num) for num in my_list]
    return set(my_list)

def menu():
    print("1. Intersection")
    print("2. Union")
    print("3. Difference")
    print("4. Quit")
    option = int(input("Set operation: "))
    return option

def set_intersection(set_1, set_2):
    return set_1 & set_2

def set_union(set_1, set_2):
    return set_1 | set_2

def set_difference(set_1, set_2):
    return set_1 - set_2

# Main
list_1 = input("Input a list of integers separated with a comma: ").strip().split(',')
list_2 = input("Input a list of integers separated with a comma: ").strip().split(',')

set_1 = make_set(list_1)
set_2 = make_set(list_2)
print(set_1)
print(set_2)

while True:
    option = menu()
    if option == 1: # Intersection
        print(set_intersection(set_1, set_2))
    elif option == 2: # Union
        print(set_union(set_1, set_2))
    elif option == 3: # Difference
        print(set_difference(set_1, set_2))
    elif option == 4:
        break