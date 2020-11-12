import string
from operator import itemgetter

def open_file(file_name):
    file_object = open(file_name, "r")
    return file_object

def create_list(file_object):
    my_list = []
    for line in file_object:
        line = line.strip().lower().split()
        my_list += line
    my_list = [word.strip(string.punctuation) for word in my_list]
    return my_list

def create_bigram_list(my_list):
    list_temp = []
    tuple_list = []
    index = 0
    
    for word in my_list:
        try:
            list_temp.append(word)
            list_temp.append(my_list[index+1])
            index += 1

            tuple_list.append(tuple(list_temp))
            list_temp.clear()
        except IndexError:
            pass

    return tuple_list

def list_to_dict(new_list):
    biagram_dict = {}

    for tuple_item in new_list:
        if tuple_item in biagram_dict:
            biagram_dict[tuple_item] += 1
        else:
            biagram_dict[tuple_item] = 1
    
    sorted_bigrams = sorted(biagram_dict.items())
    sorted_bigrams = sorted(sorted_bigrams, key=itemgetter(1), reverse=True)
    print(sorted_bigrams[:10])

# Main
file_name = input("Enter name of file: ")
#file_name = 'test.txt'

file_object = open_file(file_name)
list_words = create_list(file_object)
new_list = create_bigram_list(list_words)
list_to_dict(new_list)