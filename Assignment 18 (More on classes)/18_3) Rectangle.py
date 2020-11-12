class Rectangle:
    def __init__(self, length=1, width=1):
        if length <= 0:
            self.length = 1
        else:
            self.length = length
        
        if width <= 0:
            self.width = 1
        else:
            self.width = width

    def __str__(self):
        return "Length: {}, Width: {}".format(self.length, self.width)

    def area(self):
        area = self.length * self.width
        return area

    def perimeter(self):
        perimeter = (self.length * 2) + (self.width * 2)
        return perimeter

    def __repr__(self):
        return "Rectangle({},{})".format(self.length, self.width)
    
    def __eq__(self, other):
        return self.area() == other.area()