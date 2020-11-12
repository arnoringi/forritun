# Your functions here
def open_file(filename):
    try:
        file_object = open(filename)
        return file_object
    except:
        return None

def find_longest(file_object):
    longest = ''

    for line in file_object:
        if len(line) > len(longest):
            line = line.strip()
            longest = line
        else:
            continue
    return longest

# Main program starts here
filename = input("Enter filename: ")
file_object = open_file(filename)
if file_object:
    longest_word = find_longest(file_object)
    print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
    file_object.close()
else:
    print("File not found")