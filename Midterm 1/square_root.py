# 4. Square root

import math

start_int = int(input("Input starting integer: "))
num = start_int

while num >= 2:
    num = math.sqrt(num)
    print(round(num, 4))