a_str = input("Input a string: ")
a_str = a_str + ' '

count_words = 0
count_letters = 0

for char in a_str:
    if char == ',' or char == '.' or char == '-':
        a_str = a_str.replace(char, "")
    elif char == ' ':
        count_words += 1
    else:
        count_letters += 1

print("No. of letters: " + str(count_letters) + ", no. of words: " + str(count_words))