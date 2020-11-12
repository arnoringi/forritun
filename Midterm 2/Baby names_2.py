def open_file(file_name):
    """ Opens file """
    try:
        file_object = open(file_name, "r")
        return file_object
    except:
        return None

def process_list(file_object, k=2):
    """ Puts the first k objects into one list """
    name_list = []
    list_temp = []
    counter = 0

    for line in file_object: # Puts first k lines in one list
        list_temp.append(line)
        name_list.append(list_temp)
        list_temp = []

        counter += 1
        if counter >= k:
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
    
def five_boy_names(file_object):
    pass



def close_file(file_object):
    return file_object.close()

# Main program starts here
file_name = input("Enter file name: ").strip()
file_object = open_file(file_name)

if file_object == None:
    print("File", file_name, "not found")
else:
    # Get first two lines of file
    one_list = process_list(file_object)
    split_list = split_list(one_list)
    final_list(split_list)
    close_file(file_object)

    # Get first 5 boy names
    file_object = open(file_name)
    boy_names = process_list(file_object, 5)
    split_list = split_list(boy_names)
    final_list(split_list)