n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
if n > 1:
    for i in range (2, n):
        if (n % i) == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")