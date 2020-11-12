class Distribution:
    def __init__(self, file_stream='', distribution=''):
        ''' Create a dict of numbers upon creation'''
        self.a_dict = {}

        if file_stream != '':
            for line in file_stream:
                line.strip().split()
                for number in line:
                    if number in self.a_dict:
                        self.a_dict[number] += 1
                    else:
                        self.a_dict[number] = 1
        elif distribution != '':
            self.a_dict = distribution
    
    def __str__(self):
        ''' Prints out distribution '''
        return self.create_list()

    def create_list(self):
        ''' Creates a list for printing '''
        self.new_list = []
        self.print_list = []

        self.list_dict = self.a_dict.items()
        for item in self.list_dict:
            self.new_list.append(item)
        self.new_list.sort()

        for item in self.new_list:
            self.value = ((str(item[0]) + ': ' + str(item[1]) + '\n')) # Add all items together in an orderly manner
            self.print_list.append(self.value)
        self.print_list = "".join(self.print_list)
        return self.print_list
        
    def set_distribution(self,distribution):
        self.__init__('',distribution)

    def average(self):
        self.new_list = []
        self.total = 0

        self.list_dict = self.a_dict.items()
        for item in self.list_dict:
            self.new_list.append(item)
        self.new_list.sort()

        for item in self.new_list:
            self.total += item[0]
        
        return self.total/len(self.new_list)








# def open_file(filename):
#         ''' Returns a file stream if filename found, otherwise None '''
#         try:
#             file_stream = open(filename, "r")
#             return file_stream
#         except FileNotFoundError:
#             return None

dist1 = Distribution()
dist1.set_distribution({1:5, 2:3, 3:7, 4:4, 5:6, 6:4}) # 1 appears 5 times, 2 appears 3 times, etc.
print("Dist1: ")
print(dist1)
print(dist1.average())

# filename = input("Enter filename: ")
# file_stream = open_file(filename)

# dist2 = Distribution(file_stream)
# print("\nDist2: ")
# print(dist2)
# print(dist2.average())

# if dist1 >= dist2:
#     print("Dist1 >= Dist2")
# else:
#     print("Dist2 > Dist1")

# dist3 = dist1 + dist2
# print("\nDist3: ")
# print(dist3)
# print(dist3.average())