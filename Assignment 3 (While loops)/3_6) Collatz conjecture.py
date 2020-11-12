a0 = int(input("Input a positive int: "))   # Do not change this line
print(a0)

while a0 > 1:
    if a0 % 2 == 0:
        an = int(a0 / 2)
        print(an)
        a0 = an
    else:
        an = int((a0 * 3) + 1)
        print(an)
        a0 = an