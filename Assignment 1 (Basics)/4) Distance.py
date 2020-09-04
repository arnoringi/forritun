import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line

# convert strings to ints
x1_str = int(x1_str)
y1_str = int(y1_str)
x2_str = int(x2_str)
y2_str = int(y2_str)

d = math.sqrt((x2_str - x1_str)**2 + (y2_str - y1_str)**2)
print("d =",d)  # do not change this line