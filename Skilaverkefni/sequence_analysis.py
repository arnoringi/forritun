def process_all_files(filename_list):
    """ Takes in all files entered and processes them """
    for file_nr in range(len(filename_list)):
        # Choosing the file number n
        file_n = filename_list[file_nr]

        # Opening file number n and creating list with digits
        file_object = open_file(file_n)
        float_list = list_create(file_object)

        # Tasks
        sequence(float_list)
        cumulative_sum(float_list)
        sorted_list = sorted_sequence(float_list)
        median(sorted_list)

        # Closing file number n
        close_file(file_object)
    return None


def open_file(file_name):
    """ Opens file """
    try:
        file_object = open(file_name, "r")
        print("\nFile", file_name)
        return file_object
    except:
        print("\nFile", file_name, "not found")


def list_create(file_object):
    """ Creates a float list of digits from a file """
    float_list = []
    
    for line in file_object: # Adding line to sequence_list
        line = line.strip()

        try:
            float_digit = float(line)
            float_list.append(float_digit)
        except ValueError:
            pass
    return float_list


def sequence(float_list):
    """ Prints out sequence of file_n """
    print("\tSequence:")
    print("\t\t", end='')
    for n in range(len(float_list)):
        print(float_list[n], end=' ')
    return float_list


def cumulative_sum(float_list):
    """ Calculates and prints out the cumulative sum of file_n """
    c_sum = 0

    print("\n\tCumulative sum:")
    print("\t\t", end ='')
    for n in range(len(float_list)): # Adds next digit in list to previous and prints
        c_sum += float_list[n]
        print(round(c_sum, 1), end=' ')
    return float_list


def sorted_sequence(float_list):
    """ Sorts and prints out file_n from lowest to highest """
    sorted_list = []

    print("\n\tSorted sequence:")
    print("\t\t", end='')
    try:
        print(min(float_list), end=' ')

        sorted_list.append(min(float_list))
        float_list.remove(min(float_list))
        
        for n in range(len(float_list)): # Removes min and prints new min
            print(min(float_list), end=' ')
            sorted_list.append(min(float_list))
            float_list.remove(min(float_list))
    except ValueError:
        pass
    return sorted_list


def median(sorted_list):
    """ Finds and prints median of file_n """
    print("\n\tMedian:")
    print("\t\t", end='')
    try:
        if (len(sorted_list) % 2) == 0: # If list is an even number
            med_index1 = len(sorted_list) // 2
            med_index2 = med_index1 - 1
            find_med = (sorted_list[med_index1] + sorted_list[med_index2]) / 2
        else: # If list is an odd number
            med_index = len(sorted_list) // 2
            find_med = sorted_list[med_index]
        print(round((find_med), 2))
    except IndexError:
        pass
    return sorted_list


def close_file(file_object):
    """ Closes file_n """
    return file_object.close()


# Main program starts here
filename_list = input("Enter filenames: ").split()
process_all_files(filename_list)