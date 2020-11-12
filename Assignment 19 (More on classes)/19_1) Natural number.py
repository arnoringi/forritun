class NaturalNumber:
    def __init__(self, number=0):
        if number == str(number) or number < 0:
            self.__num = None
        else:
            self.__num = number

    def __str__(self):
        return str(self.__num)

    def __add__(self, other):
        try:
            number = self.__num + other.__num
            return NaturalNumber(number)
        except TypeError:
            return NaturalNumber("Invalid")

    def __sub__(self, other):
        try:
            number = self.__num - other.__num
            return NaturalNumber(number)
        except TypeError:
            return NaturalNumber("Invalid")

    def __mul__(self, other):
        try:
            number = self.__num * other.__num
            return NaturalNumber(number)
        except TypeError:
            return NaturalNumber("Invalid")



# num1 = NaturalNumber(1)
# print(num1)

# num1 = NaturalNumber(3)
# num2 = NaturalNumber(4)
# num3 = num1 + num2
# print(num3)

# num2 = NaturalNumber(2)
# num3 = num1 * num2
# print(num3)

# num3 = num1 - num3
# print(num3)