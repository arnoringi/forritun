def menu_selection():
    print("Menu:")
    choice = input("(a)dd, (r)emove, (f)ind: ").lower()
    return choice

def execute_selection(choice, a_dict):
    def add_to_dict(a_dict):
        key = input("Key: ").strip()
        value = input("Value: ").strip()
        
        if key in a_dict:
            return None
        else:
            a_dict[key] = value
            return a_dict

    def remove_from_dict(a_dict):
        key_rem = input("Key to remove: ").strip()

        if key_rem in a_dict:
            a_dict.pop(key_rem)
            return a_dict
        else:
            return None

    def find_key(a_dict):
        key_find = input("Key to locate: ")

        if key_find in a_dict:
            return a_dict[key_find]
        else:
            return None

    if choice == 'a':
        value_a = add_to_dict(a_dict)
        if value_a == None:
            print("Error. Key already exists.")
        
    elif choice == 'r':
        value_r = remove_from_dict(a_dict)
        if value_r == None:
            print("Key not found.")
    
    elif choice == 'f':
        value_f = find_key(a_dict)
        if value_f == None:
            print("Key not found.")
        else:
            print("Value:", value_f)
    else:
        print("Invalid choice")

    return a_dict

def dict_to_tuples(a_dict):
    list_dict = a_dict.items()
    dict_list = []

    for item in list_dict:
        dict_list.append(item)
    
    return dict_list    

def main():
    more_input = True
    a_dict = {}
    
    while more_input:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more_input = again.lower() == 'y'
    
    tuple_list = dict_to_tuples(a_dict)
    print(sorted(tuple_list))

main()