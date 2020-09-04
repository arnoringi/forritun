num1 = int(input("First number: ")) # Do not change this line
num2 = int(input("Second number: ")) # Do not change this line
num3 = int(input("Third number: ")) # Do not change this line

if num1 < num2:
    if num1 < num3:
        min_int = num1
elif num2 < num1:
    if num2 < num3:
        min_int = num2
    else:
        min_int = num3
else:
        min_int = num3
        
print("The minimum is: ", min_int) # Do not change this line