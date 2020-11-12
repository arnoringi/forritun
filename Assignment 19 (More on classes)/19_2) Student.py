class Student:
    def __init__(self, student_id, grades):
        self.student_id = student_id
        self.grades = grades
    
    def __str__(self):
        return "Student ID: {}\nGrades: {}".format(self.student_id, self.grades)

    def get_average(self):
        average = 0
        for grade in self.grades:
            average += grade
        
        return average/len(self.grades)

    def __lt__(self, other):
        str_bool = bool(self.get_average() < other.get_average())
        return str_bool



# student1 = Student(1, [3.0, 4.6, 3.4, 5.4])
# student2 = Student(2, [9.5, 9.0, 8.9, 9.8])

# print(student1)
# if student1 < student2:
#     print("student1 < student2")