num = int(input("Input an int: ")) # You can copy this line but not change it
count = 0

# Fill in the missing code below
while num != 10:
    count += num
    num = int(input("Input an int: "))
else:
    print(count)