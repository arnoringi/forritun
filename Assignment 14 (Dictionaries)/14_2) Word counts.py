import string

def get_word_list(file_object):
    word_list = []
    
    for line in file_object:
        line = line.strip().split()
        for word in line:
            word = word.strip(string.punctuation)
            word = word.lower()
            word_list.append(word)
    
    word_list.sort()
    return word_list

def word_list_to_counts(word_list):
    word_count_dict = {}

    for word in word_list:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    
    return word_count_dict

def dict_to_tuples(word_count_dict):
    list_dict = word_count_dict.items()
    dict_list = []

    for item in list_dict:
        dict_list.append(item)
    
    return dict_list

def main():
    filename = input("Name of file: ")
    file_object = open(filename)
    word_list = get_word_list(file_object) 
    file_object.close()
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuples(word_count_dict)
    print(sorted(word_count_tuples))
    
main()