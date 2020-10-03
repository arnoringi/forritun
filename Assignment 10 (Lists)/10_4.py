def open_file(file_name):
    file_object = open(file_name, "r")
    return file_object

def list_create(file_object):
    my_list = []

    for line in file_object:
        new_list = line.split()
        my_list.append(new_list)

    print(my_list)
    return my_list

# Main starts here
def main():
    file_name = "vectors.txt"
    file_object = open_file(file_name)
    list_create(file_object)
    print(list_create)

main()