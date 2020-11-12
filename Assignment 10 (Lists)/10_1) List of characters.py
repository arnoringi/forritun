def list_splice(sentence):
    my_list = []

    for char in sentence:
        my_list.append(char)

    return my_list

# The main program starts here
sentence = input("Input a sentence: ")

my_list = list_splice(sentence)
print(my_list)

my_list.sort()
print(my_list)