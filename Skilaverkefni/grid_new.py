class Grid:
    INC = 1 # Increase by
    first = True

    y_cord = 1
    x_cord = 0
    tuple_item = (y_cord, x_cord)
    new_tuple = (y_cord, x_cord)

    y = 0
    x = 0

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.grid = ""
    
    def __str__(self):
        ''' Returns initial grid as string '''
        if self.grid == '':
            for row in range(self.row):
                for column in range(self.column):
                    if self.first: # Adding pos(1,1)
                        self.first = False
                        self.grid += 'x'
                    else: # Adding rest of grid
                        self.grid += 'o'
                self.grid += '\n'
            return self.grid
        else:
            self.grid = self.new_tuple.current_pos()
            return self.grid

    def new_grid(self):
        ''' Creates new grid '''
        self.grid = ''
        self.index = 1
        self.line_index = 1

        for row in range(self.row):
            for column in range(self.column):
                if self.index == self.new_tuple[1] and self.line_index == self.new_tuple[0]:
                    self.grid += 'x'
                else:
                    self.grid += 'o'
            self.grid += '\n'
        return self.grid

    def current_pos(self):
        ''' Find 'x' in string '''
        for x in self.grid:
            if x == '\n':
                self.x_cord = 0 # Reset
                self.y_cord += self.INC
            elif x == 'o':
                self.x_cord += self.INC
            elif x == 'x':
                self.x_cord += self.INC
                self.tuple_item = (self.y_cord, self.x_cord)
                return tuple(self.tuple_item)

    def move_left(self):
        ''' Moves 'x' to the left by one '''
        self.y = self.tuple_item[0]
        self.x = self.tuple_item[1]

        if self.x == self.row:
            self.x = 1
        else:
            self.x += self.INC
        # self.tuple_item = (self.y, self.x)
        self.new_tuple = tuple((self.y, self.x))
        return self.new_tuple

a_grid = Grid(3,4)
print(a_grid)
print(a_grid.current_pos())
a_grid.move_left()
print(a_grid)