# The function definition goes here
def mixer(input):
    return input[::2]

input_str = input("Enter a string: ")

# You call the function here
print("Every other character:",mixer(input_str))