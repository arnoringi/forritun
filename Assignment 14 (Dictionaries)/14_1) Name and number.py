def add_to_dict(number, name, my_dict):
    my_dict[name] = number
    return my_dict

# Main program starts here
my_dict = {}
while True:
    name = input("Name: ").strip()
    number = input("Number: ").strip()

    my_dict = add_to_dict(number, name, my_dict)

    more_data = input("More data (y/n)? ").lower()
    if more_data == 'n':
        list_dict = my_dict.items()
        new_list = []
        for item in list_dict:
            new_list.append(item)

        new_list.sort()
        print(new_list)
        break
    else:
        continue
