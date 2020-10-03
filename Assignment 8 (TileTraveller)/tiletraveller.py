def tile1_1(x): #Starter tile #N
    print("You can travel: (N)orth.")
    direction = input("Direction: ")
    direction = direction.lower()

    if direction == 'n':
        return tile1_2(x)
    else:
        print("Not a valid direction!")
        return tile1_1(x)

def tile1_2(x): #NES
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    direction = input("Direction: ")
    direction = direction.lower()

    if direction == 'n':
        return tile1_3(x)
    if direction == 'e':
        return tile2_2(x)
    if direction == 's':
        return tile1_1(x)
    else:
        print("Not a valid direction!")
        return tile1_2(x)

def tile1_3(x): #ES
    print("You can travel: (E)ast or (S)outh.")
    direction = input("Direction: ")
    direction = direction.lower()

    if direction == 'e':
        return tile2_3(x)
    if direction == 's':
        return tile1_2(x)
    else:
        print("Not a valid direction!")
        return tile1_3(x)

def tile2_1(x): #N
    print("You can travel: (N)orth.")
    direction = input("Direction: ")
    direction = direction.lower()

    if direction == 'n':
        return tile2_2(x)
    else:
        print("Not a valid direction!")
        return tile2_1(x)

def tile2_2(x): #SW
    print("You can travel: (S)outh or (W)est.")
    direction = input("Direction: ")
    direction = direction.lower()

    if direction == 's':
        return tile2_1(x)
    if direction == 'w':
        return tile1_2(x)
    else:
        print("Not a valid direction!")
        return tile2_2(x)

def tile2_3(x): #EW
    print("You can travel: (E)ast or (W)est.")
    direction = input("Direction: ")
    direction = direction.lower()

    if direction == 'e':
        return tile3_3(x)
    if direction == 'w':
        return tile1_3(x)
    else:
        print("Not a valid direction!")
        return tile2_3(x)

def tile3_1(x): #Final tile
    print("Victory!")

def tile3_2(x): #NS
    print("You can travel: (N)orth or (S)outh.")
    direction = input("Direction: ")
    direction = direction.lower() 

    if direction == 'n':
        return tile3_3(x)
    if direction == 's':
        return tile3_1(x)
    else:
        print("Not a valid direction!")
        return tile3_2(x)

def tile3_3(x): #SW
    print("You can travel: (S)outh or (W)est.")
    direction = input("Direction: ")
    direction = direction.lower()

    if direction == 's':
        return tile3_2(x)
    if direction == 'w':
        return tile2_3(x)
    else:
        print("Not a valid direction!")

#To initiate the program
x = 0
start = tile1_1(x)