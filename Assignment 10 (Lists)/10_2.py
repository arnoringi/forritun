import string

# Implement a function here
def list_letters(sentence):
    my_list = []

    for char in sentence:
        if char.isalpha() and char not in my_list:
            my_list.append(char)
        else:
            continue
        

    return my_list

# Main starts here
sentence = input("Input a sentence: ")
unique_letters = list_letters(sentence)

# Call the function here
print("Unique letters:", unique_letters)