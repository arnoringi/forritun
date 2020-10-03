# Your functions should appear here
def new_list(my_list):
    new_list = []

    for word in my_list:
        if len(word) <= 1 or word.isdigit():
            continue
        else:
            new_list.append(word)

    return new_list

def first_last(new_list):
    for word in new_list:
        if word[:1] == word[-1:]:
            print(word)
        else:
            continue

# Main program starts here
# It should mostly be a sequence of function calls

def main():
    my_list = []

    while True:
        input_str = input("Enter word to be added to list: ")

        if input_str != 'x':
            my_list.append(input_str)
        else:
            break
    
    print(my_list)
    first_last(new_list(my_list))

main()