# max_of_three function definition goes here
def max_of_three(first, second, third):
    maximum = first
    if second > first and second > third:
        maximum = second
    elif third > first and third > second:
        maximum = third
    return maximum

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

# Call the function here
maximum = max_of_three(first, second, third)
print("Maximum:", maximum)