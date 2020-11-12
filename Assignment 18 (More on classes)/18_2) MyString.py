class MyString:
    def __init__(self, string):
        self.string = string
    
    def __str__(self):
        return str(self.string)

    def __sub__(self, other):
        str_sub = abs(len(self.string) - len(other.string))
        return str_sub

    def __gt__(self, other):
        str_bool = bool(len(self.string) > len(other.string))
        return str_bool