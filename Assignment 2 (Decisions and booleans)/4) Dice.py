d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

if (d1 >= 1 and d1 <= 6) and (d2 >= 1 and d2 <=6):
    if d1 == d2:
        print("Pair")
    else:
        print(d1 + d2)
else:
    print("Invalid input")