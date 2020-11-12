# palindrome function definition goes here
def palindrome(string):
    SPECIAL = """ .,:;?!_-"'()"""
    is_true = False

    for char in string:
        for digits in SPECIAL:
            if char == digits:
                string = string.replace(char, "")

    for char in string:
        if char == char.upper():
            string = string.replace(char, char.lower())
    
    if string == string[::-1]:
        is_true = True
    return is_true

in_str = input("Enter a string: ")

# call the function and print out the appropriate message
if palindrome(in_str) == True:
    print('"' + in_str + '" is a palindrome.')
else:
    print('"' + in_str + '" is not a palindrome.')