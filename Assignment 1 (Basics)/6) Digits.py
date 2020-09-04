n_str = input("Input n: ")
# remember to convert to an int
n_str = int(n_str)

first_three = n_str // 100
last_two = n_str % 100

print("first_three:", first_three)
print("last_two:", last_two)