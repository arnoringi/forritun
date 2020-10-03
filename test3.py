import math

num = int(input("num: "))

while num != 'q':
    num1 = num % 16
    num2 = num // 16

    print("Modulus:", num1)
    print("Afgangur:", num2)
    print()
    num = int(input("num: "))