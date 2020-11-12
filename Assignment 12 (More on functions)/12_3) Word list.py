import string

def open_file(file_name):
    """ Opens file """
    file_object = open(file_name, 'r')
    return file_object

def line_list(file_object):
    """ Creates a list with every word/punctuation """
    line_list = []

    for line in file_object:
        line = line.strip()
        ls = line.split()
        for char in ls:
            line_list.append(char)
    
    return line_list
    
def sort_list(line_list):
    """ Sorts and removes unwanted words/characters """
    unique_list = []
    new_list = []

    # Remove punctuation
    for word in line_list:
        for char in string.punctuation:
            word = word.strip(char)
            if char == word:
                word.replace(char, '')
        word = word.replace('"', '') # Odd character
        new_list.append(word)
        
    # Sort alphabetical
    new_list.sort()

    # Remove repeats
    for word in new_list:
        if word not in unique_list:
            unique_list.append(word)
    
    print(unique_list)

# Main program starts here
file_name = input("Enter filename: ").strip()
file_object = open_file(file_name)

new_list = line_list(file_object)
sort_list(new_list)