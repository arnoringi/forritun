a_str = input("Input a string: ")

count_lower = 0
count_upper = 0

for letter in a_str:
    if letter == ' ' or letter == '.' or letter == ',':
        continue
    if letter == letter.lower():
        count_lower += 1
    if letter == letter.upper():
        count_upper += 1
print(count_lower)
print(count_upper)