year = int(input("Input a year: ")) # Do not change this line

# Fill in the missing code below
if year % 4 == 0: #S1
    if year % 100 == 0: #S2
        if year % 400 == 0: #S3
            print("True")
        else:
            print("False")
    else: #S4
        print("True")
else: #S5
    print("False")