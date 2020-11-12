# Your function definition goes here
def count_digits(string):
    count = 0

    for char in string:
        if char.isdigit():
            count += 1
        else:
            continue
    return count

input_str = input("Enter a string: ")

# Call the function here
digit_count = count_digits(input_str)

print("No. of digits:", digit_count)