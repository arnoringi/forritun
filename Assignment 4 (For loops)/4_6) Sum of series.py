length = int(input("Input the length of series: "))
length *= 2
summa = 0

for i in range(2, length+1, 2):
    if i % 4 == 0:
        i = i - (i * 2)
        print(i)
        summa += i
    else:
        print(i)
        summa += i

print("Sum:",summa)