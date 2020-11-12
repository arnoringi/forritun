class Grid():
    INC = 1 # Increase by
    DEC = 1 # Decrease by

    first = True
    stop = False

    x_cord = 0
    y_cord = 1
    tuple_item = (y_cord, x_cord)

    index = 0
    line_index = 0
    grid_list = []
    temp_list = []

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.grid = ""

    def __str__(self):
        ''' Returns grid as string '''
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
        if len(self.grid) == 1:
            return self.grid
        else:
            self.line_index = 0 # Reset line index
            self.stop = False # Reset stop boolean

            self.grid_list = self.grid.split() # Creates list of lines
            for line in self.grid_list:
                self.temp_list = list(line) # Creates list of elements in line
                self.index = 0 # Reset index
                for x in self.temp_list:
                    if x == 'x':
                        self.temp_list[self.index] = 'o' # Change 'x' into 'o'
                        if self.index == 0: # If on edge
                            self.temp_list[self.index + (self.column - self.DEC)] = 'x'
                            self.stop = True
                            break
                        else:
                            self.temp_list[self.index - self.DEC] = 'x'
                            self.stop = True
                            break
                    else:
                        self.index += self.INC
                self.grid_list[self.line_index] = ''.join(self.temp_list) # Replace line with altered line
                if self.stop: # Stop completely
                    break
                else:
                    self.line_index += self.INC
            self.grid = '\n'.join(self.grid_list)
            self.grid += '\n' # Add newline to end of string
            return self.grid

    def move_right(self):
        ''' Moves 'x' to the right by one '''
        if len(self.grid) == 1:
            return self.grid
        else:
            self.line_index = 0 # Reset line index
            self.stop = False # Reset stop boolean

            self.grid_list = self.grid.split() # Creates list of lines
            for line in self.grid_list:
                self.temp_list = list(line) # Creates list of elements in line
                self.index = 0 # Reset index
                for x in self.temp_list:
                    if x == 'x':
                        self.temp_list[self.index] = 'o' # Change 'x' into 'o'
                        if self.index == (self.column - self.DEC): # If on edge
                            self.temp_list[0] = 'x' # Start of line
                            self.stop = True
                            break
                        else:
                            self.temp_list[self.index + self.INC] = 'x'
                            self.stop = True
                            break
                    else:
                        self.index += self.INC
                self.grid_list[self.line_index] = ''.join(self.temp_list) # Replace line with altered line
                if self.stop: # Stop completely
                    break
                else:
                    self.line_index += self.INC
            self.grid = '\n'.join(self.grid_list)
            self.grid += '\n' # Add newline to end of string
            return self.grid

    def move_up(self):
        ''' Moves 'x' up by one '''
        if len(self.grid) == 1:
            return self.grid
        else:
            self.line_index = 0 # Reset line index
            self.stop = False # Reset stop boolean

            self.grid_list = self.grid.split() # Creates list of lines
            for line in self.grid_list:
                self.temp_list = list(line) # Creates list of elements in line
                for x in self.temp_list:
                    if x == 'x':
                        if self.line_index == 0: # If on edge
                            self.grid_list[self.row - self.DEC] = self.grid_list[self.line_index]
                            self.grid_list[self.line_index] = 'o' * self.column
                            self.stop = True
                            break
                        else:
                            self.grid_list[self.line_index - self.DEC] = self.grid_list[self.line_index]
                            self.grid_list[self.line_index] = 'o' * self.column
                            self.stop = True
                            break
                    else:
                        pass
                if self.stop: # Stop completely
                    break
                else:
                    self.line_index += self.INC
            self.grid = '\n'.join(self.grid_list)
            self.grid += '\n' # Add newline to end of string
            return self.grid

    def move_down(self):
        ''' Moves 'x' down by one '''
        if len(self.grid) == 1:
            return self.grid
        else:
            self.line_index = 0 # Reset line index
            self.stop = False # Reset stop boolean

            self.grid_list = self.grid.split() # Creates list of lines
            for line in self.grid_list:
                self.temp_list = list(line) # Creates list of elements in line
                for x in self.temp_list:
                    if x == 'x':
                        if self.line_index == (self.row - self.DEC): # If on edge
                            self.grid_list[0] = self.grid_list[self.line_index]
                            self.grid_list[self.line_index] = 'o' * self.column
                            self.stop = True
                            break
                        else:
                            self.grid_list[self.line_index + self.INC] = self.grid_list[self.line_index]
                            self.grid_list[self.line_index] = 'o' * self.column
                            self.stop = True
                            break
                    else:
                        pass
                if self.stop: # Stop completely
                    break
                else:
                    self.line_index += self.INC
            self.grid = '\n'.join(self.grid_list)
            self.grid += '\n' # Add newline to end of string
            return self.grid

a_str = Grid(3,4)
print(a_str)