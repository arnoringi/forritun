def open_file(file_name):
    file_object = open(file_name)
    return file_object

def split_line(file_object):
    word = ''
    
    for line in file_object:
        for char in line:
            if char == ' ' or char == '\n':
                print(word)
                word = ''
            else:
                word += char
    print(word)

# Main program starts here
filename = input("Enter filename: ")
file_object = open_file(filename)
split_line(file_object)
