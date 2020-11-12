import string

def open_collection(collection):
    ''' Opens collection for user '''
    try:
        file_object = open(collection, "r")
        return file_object
    except FileNotFoundError:
        return None

def menu():
    ''' Prints out options and returns input for user '''
    print("\nWhat would you like to do?")
    print("1. Search Documents\n2. Print Document\n3. Quit Program")
    choice = input("> ").strip()
    return choice

def convert_to_string(file_object):
    ''' Converts the collection into a list of strings '''
    list_of_strings = []
    temp_list = []                  

    for line in file_object:
        if line.strip() == "<NEW DOCUMENT>": # Seperate documents
            process_line(temp_list, list_of_strings)
            temp_list.clear()
        else:
            line = line.strip().lower().split()
            temp_list += line
    process_line(temp_list, list_of_strings)
    return list_of_strings

def process_line(temp_list, list_of_strings):
    ''' Takes lists from 'convert_to_string' and adds everything together '''
    temp_string = ''

    temp_list = [word.strip(string.punctuation) for word in temp_list] # Strip punctuation
    for word in temp_list:
        temp_string += word
        temp_string += ' '
    list_of_strings.append(temp_string.strip()) # Append a file (long string) to list

def create_dictionary(list_of_strings):
    ''' Creates dictionary of words appearing in each file '''
    word_dict = {}
    document_num = 0

    for document in list_of_strings:
        temp_list = document.split()
        for word in temp_list:
            if word in word_dict:
                value = word_dict[word]
                value.add(str(document_num))
                word_dict[word] = value
            else:
                word_dict[word] = set(str(document_num)) # Having document_num as string, since 'set' can't iterate through int
        document_num += 1
    return word_dict

def search_documents(dictionary):
    ''' Option 1: Searches for specific word(s) in documents '''
    SEARCH_LEN = 1
    search_words = input("Enter search words: ").strip().lower().split()
    in_dictionary = set()
    first = True

    if len(search_words) == SEARCH_LEN: # If only 1 search word
        try:
            value = dictionary[search_words[0]]
            in_dictionary = value
            print_search_document(in_dictionary)
        except KeyError:
            print_search_document(set()) # Reset set, since no match
    else: # If 2 or more search words
        try:
            for word in search_words:
                value = dictionary[word]
                if first == True:
                    in_dictionary = value
                    first = False
                else:
                    in_dictionary = in_dictionary & value
            print_search_document(in_dictionary)                
        except KeyError:
            print_search_document(set()) # Reset set, since no match

def print_search_document(in_dictionary):
    ''' Prints documents that fit the search term, from 'search_documents' '''
    if in_dictionary != set(): # If set is not empty or incorrect
        print("Documents that fit search: ", end='')
        list_dictionary = list(in_dictionary)
        list_dictionary = sorted([int(num) for num in list_dictionary]) # Change to int to sort in increasing order
        list_dictionary = [str(num) for num in list_dictionary] # Change back to string to join list
        document_string = ' '.join(list_dictionary)
        print(document_string)
    else:
        print("No match.")

def print_documents(file_object, doc_collection):
    ''' Option 2: Prints out desired document from document collection '''
    file_object = reopen_documents(file_object, doc_collection)
    print_number = input("Enter document number: ").strip()
    doc_number = 0
    first = True
    
    for line in file_object:
        if line.strip() == "<NEW DOCUMENT>":
            doc_number += 1
        elif doc_number == int(print_number): # Doc number matches input
            if first == True:
                print("Document #" + print_number)
                print(line.strip())
                first = False
            else:
                print(line.strip())
    if int(print_number) > doc_number:
        print("No match.")

def reopen_documents(file_object, doc_collection):
    ''' Reopens document collection '''
    file_object.close()
    file_object = open_collection(doc_collection)
    return file_object


# Main program starts here
doc_collection = input("Document collection: ").strip().lower()
file_object = open_collection(doc_collection)

if file_object == None: # Collection not found
    print("Documents not found.")
    pass
else:
    list_of_strings = convert_to_string(file_object)
    dictionary = create_dictionary(list_of_strings)

    while True: # User picks an option until they want to quit
        choice = menu()
        if choice == '1':       # 1. Search documents
            search_documents(dictionary)
        elif choice == '2':     # 2. Print documents
            print_documents(file_object, doc_collection)
        else:                   # 3. Quit the program
            print("Exiting program.")
            break