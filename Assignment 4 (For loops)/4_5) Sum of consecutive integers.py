num = int(input("Input an int: ")) # Do not change this line
summa = 1

for i in range(1, num+1):
    print(summa)
    for j in range(i, i+1):
        summa += j+1