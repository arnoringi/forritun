def open_file(file_name):
    ''' Opens file '''
    try:
        file_object = open(file_name, "r")
        return file_object
    except FileNotFoundError:
        print("File", file_name, "not found")

def read_file_parts(file_object):
    ''' Reads and processes grade parts from file 1 '''
    list_of_parts = []
    tuple_list = [] # Temp list that converts to tuple
    counter = 1

    # Create two lists
    for line in file_object:
        if counter == 1: # Create list for line 1
            line_1 = line.strip().split()
            counter += 1
        elif counter == 2: # Create list for line 2
            line_2 = line.strip().split()
            line_2 = [float(num) for num in line_2] # Change all digits to float in list
    
    # Create tuples
    for index in range(5):
        tuple_list.append(line_1[index])
        tuple_list.append(line_2[index])
        list_of_parts.append(tuple(tuple_list))
        tuple_list = [] # Reset

    print(list_of_parts)
    return list_of_parts

def read_file_grades(file_object):
    ''' Reads and processes info about students and grades from file 2 '''
    student_grades = []
    tuple_list = [] # Temp list that converts to tuple

    for line in file_object:
        line_list = line.strip().split()
        
        tuple_list.append(line_list[0]) # Add first element (name@email)
        line_list.remove(line_list[0])

        line_list = [float(num) for num in line_list]
        tuple_list.append(line_list) # Add list of grades
        student_grades.append(tuple(tuple_list))
        tuple_list = [] # Reset

    print(student_grades)
    return student_grades

def calculate_final(student_grades, list_of_parts):
    ''' Calculates weighted course grade for each student '''
    weighted_grade = 0
    w_grade_list = []
    index = 0

    for element in student_grades: # Get grade list for specific student
        grades = element[1] # Grade list for student x

        for item in list_of_parts: # Calculate weighted grade
            weight = item[1]

            specific_grade = weight * grades[index]
            weighted_grade += specific_grade
            index += 1
        
        w_grade_list.append(weighted_grade)
        # Reset
        weighted_grade = 0
        index = 0
    
    for grade in w_grade_list: ## Only way I found to append to tuple is through lists
        temp = []
        temp.append(grade)
        student_grades[index] += tuple(temp)
        # Reset
        temp = []
        index += 1

    print(student_grades)
    print()
    return student_grades

def print_outcome(student_grades):
    ''' Prints outcome in an orderly manner '''
    ROUND = 2
    print("{:>16}{:>14}{:>14}{:>14}{:>14}{:>14}{:>14}".format("Student ID", "Quizzes", "Assignments", "Projects", "Midterms", "Final", "Course grade"))
    
    for element in student_grades:
        for item in element:
            try: # Print course grade
                item = float(item)
                item = round(item, ROUND)
                print("{:>14}".format(item))
            except ValueError: # Print student emails
                item = str(item)
                print("{:>16}".format(item), end='')
            except TypeError: # Print grade list
                for number in item:
                    print("{:>14}".format(number), end='')

def close_file(file_object_parts, file_object_grades):
    ''' Closes files '''
    file_object_parts.close()
    file_object_grades.close()
            

# Main program starts here
file_name_parts = input("Enter filename for parts: ").strip() # File 1
file_object_parts = open_file(file_name_parts)
if file_object_parts != None:
    list_of_parts = read_file_parts(file_object_parts)

    file_name_grades = input("Enter filename for grades: ").strip() # File 2
    file_object_grades = open_file(file_name_grades)
    if file_object_grades != None:    
        student_grades = read_file_grades(file_object_grades)

        calculate_final(student_grades, list_of_parts)
        print_outcome(student_grades)

        close_file(file_object_parts, file_object_grades)