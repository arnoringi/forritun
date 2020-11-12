def open_file(file_name):
    file_object = open(file_name, "r")
    return file_object

def read_and_print(file_object):
    string = ''

    for line in file_object:
        line = line.strip().replace(" ", "")
        string += line
    print(string)

# Main starts here
def main():
    file_name = input("Enter filename: ")
    file_object = open_file(file_name)
    read_and_print(file_object)

main()