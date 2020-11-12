def first_and_last(name):
    letter_list = []
    first_name_letters = []
    counter = 1

    for elem in name:
        for letter in elem:
            first_name_letters.append(letter)
        break
    
    for elem in name:
        if counter == 2:
            for letter in elem:
                if letter in first_name_letters and letter not in letter_list:
                    letter_list.append(letter)
        else:
            counter += 1

    return letter_list

def set_first_and_last(name):
    counter = 1
    for elem in name:
        if counter == 1:
            first_set = set(elem)
            counter += 1
        elif counter == 2:
            second_set = set(elem)

    return first_set & second_set

name = input("Enter name: ").lower().strip().split()
list_letter = first_and_last(name)
set_letter = set_first_and_last(name)
print(sorted(list_letter))
print(sorted(set_letter))