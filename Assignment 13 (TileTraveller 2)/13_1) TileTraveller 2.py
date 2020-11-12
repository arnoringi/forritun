# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

YES = 'y'
NO = 'p'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    if col == 3 and row == 1:
        return True, False
    else:
        return False, True

def print_directions(directions_str, coins):
    def pull_lever(coins):
        ''' Gives player a coin if lever is pulled '''
        lever = input("Pull a lever (y/n): ").lower()
        if lever == 'y':
            coins += 1
            print("You received 1 coin, your total is now " + str(coins) + ".")
            return coins
        else:
            return coins

    for ch in directions_str:
        if ch == YES:
            coins = pull_lever(coins)
            directions_str = directions_str[:-1] # Removing last character from string

    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
    return coins
        
def find_directions(col, row, path):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # TILE A (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # TILE B (1,2) ###
        valid_directions = NORTH+EAST+SOUTH
        if 'B' not in path:
            valid_directions += YES
        else:
            pass        
    elif col == 1 and row == 3: # TILE C (1,3)
        valid_directions = EAST+SOUTH 
    elif col == 2 and row == 1: # TILE D (2,1)
        valid_directions = NORTH 
    elif col == 2 and row == 2: # TILE E (2,2) ###
        valid_directions = SOUTH+WEST
        if 'E' not in path:
            valid_directions += YES
        else:
            pass        
    elif col == 2 and row == 3: # TILE F (2,3) ###
        valid_directions = EAST+WEST
        if 'F' not in path:
            valid_directions += YES
        else:
            pass        
    elif col == 3 and row == 2: # TILE G (3,2) ###
        valid_directions = NORTH+SOUTH
        if 'G' not in path:
            valid_directions += YES
        else:
            pass        
    elif col == 3 and row == 3: # TILE H (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions, path

def play_one_move(col, row, valid_directions):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
        if col == 1 and row == 2: # Changes so that player cannot pull lever again
            path.append('B')
        elif col == 2 and row == 2:
            path.append('E')
        elif col == 2 and row == 3:
            path.append('F')
        elif col == 3 and row == 2:
            path.append('G')
    else:
        col, row = move(direction, col, row)
        victory_or_game = is_victory(col, row)
        victory = victory_or_game[0]
        game = victory_or_game[1]
    return victory, game, col, row

def play_again(victory, coins, row, col, game):
    ''' Only for replays '''
    play = input("Play again (y/n): ").lower()
    if play == 'y':
        # Reset status
        path.clear()
        victory = False
        coins = 0
        row = 1
        col = 1
        game = True
        return victory, coins, row, col, game
    else:
        game = False
        return victory, coins, row, col, game



# The main program starts here
victory = False
game = True

row = 1
col = 1

coins = 0
path = []

while game == True:
    while not victory:
        valid_directions = find_directions(col, row, path)
        coins_new = print_directions(valid_directions[0], coins)
        coins = coins_new
        victory, game, col, row = play_one_move(col, row, valid_directions[0])
    else:
        print("Victory! Total coins " + str(coins) + ".")
        play = play_again(victory, coins, row, col, game)
        
        # Value change
        victory = play[0]
        coins = play[1]
        row = play[2]
        col = play[3]
        game = play[4]