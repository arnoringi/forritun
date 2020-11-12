def open_file(file_name):
    """ Opens file """
    try:
        file_object = open(file_name, "r")
        return file_object
    except:
        return None

def process_list(file_object):
    """ Puts the first two objects into one list """
    name_list = []
    list_temp = []
    counter = 0

    for line in file_object: # Puts first two lines in one list
        list_temp.append(line)
        name_list.append(list_temp)
        list_temp = []

        counter += 1
        if counter >= 2:
            break
    
    return name_list

def split_list(name_list):
    """ Splits list inside list """
    list_temp = []
    name_list_new = []
    string = ''

    for element in name_list:
        for line in element:
            for letter in line:
                if letter == '\t' or letter == '\n':
                    list_temp.append(string)
                    string = ''
                else:
                    string += letter
        name_list_new.append(list_temp)
        list_temp = []
    #rint(name_list_new)
    return name_list_new

def final_list(name_list):
    """ Finalizes list """
    list_temp = []
    name_list_final = []

    for element in name_list:
        for item in element:
            try:
                item = int(item)
                list_temp.append(item)
            except:
                list_temp.append(item)
        name_list_final.append(list_temp)
        list_temp = []
    
    print(name_list_final)

# Main program starts here
file_name = input("Enter file name: ").strip()
file_object = open_file(file_name)

if file_object == None:
    print("File", file_name, "not found")
else:
    one_list = process_list(file_object)
    split_list = split_list(one_list)
    final_list(split_list)