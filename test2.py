class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def __sub__(self, other):
        x = self.__x - other.__x
        y = self.__y - other.__y

        return Point(x,y)

p1 = Point(3,4)
p2 = Point(2,2)
p3 = p1 - p2
print(p3.get_x(), p3.get_y())