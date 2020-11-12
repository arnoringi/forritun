def open_file(file_name):
    """ Opens file """
    try:
        file_object = open(file_name, "r")
        return file_object
    except:
        return None

def find_word_count(file_object):
    """ Counts number of words in file """
    symbol_list = ['!','?',',','.']
    word_count = 0

    for line in file_object: # Goes through line
        line = line.strip().split(' ')

        for word in line: # Checks each word
            word_count += 1
            for symbol in symbol_list: # Checks if symbol is in word
                if symbol in word:
                    word_count += 1

    print(word_count)

### Main program starts here
file_name = input("Enter filename: ").strip()
file_object = open_file(file_name)

if file_object == None:
    print("File", file_name, "not found!")
else:
    find_word_count(file_object)