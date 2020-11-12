def int_sets(set_1, set_2):
    """ Changes digits in sets, into ints """
    sets = [set_1, set_2]

    # Changing numbers to int
    for set_number in sets:
        for number in range(len(set_number)):
            set_number.append(int(set_number[0]))
            set_number.remove(set_number[0])
    
    return set_1, set_2

def sort_sets(set_1, set_2):
    """ Sorts sets into increasing order and prints them """
    sets = [set_1, set_2]

    # Sorting sets
    for set_number in sets:
        set_number = set_number.sort()

    print("Set 1:", set_1)
    print("Set 2:", set_2)
    return set_1, set_2

def intersection(set_1, set_2):
    """ Finds intersection of the two sets and prints """
    intersection_list = []

    for number in set_1:
        if number in set_2:
            intersection_list.append(number)
    
    print("Intersection:", intersection_list)
    return set_1, set_2

def union(set_1, set_2):
    """ Finding the union of two sets and prints """
    union_list = []

    for number in set_2: # Adds numbers to set_1, since this is the last step
        set_1.append(number)
    
    set_1.sort()

    for number in set_1:
        if number not in union_list:
            union_list.append(number)
    
    print("Union:", union_list)
    return set_1, set_2

### Main program starts here
set_1 = input("Enter elements of a list separated by space: ").strip().split(' ')
set_2 = input("Enter elements of a list separated by space: ").strip().split(' ')

int_sets(set_1, set_2)
sort_sets(set_1, set_2)
intersection(set_1, set_2)
union(set_1, set_2)

# Á EFTIR AÐ REMOVE-A REPEATS Í LISTA, NENNIS