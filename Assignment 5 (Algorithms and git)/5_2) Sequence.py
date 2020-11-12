#1 Generates the first n numbers in a sequence
#2 We add the three most recent numbers together, n amount of times
#3 1,  2,  3,  6, 11, 20, 37, ___, ___, ___, …
#4 1, +1, +1, +3, +5, +9, +17


n = int(input("Enter the length of the sequence: ")) # Do not change this line

num1 = 1
num2 = 1
num3 = 0

for i in range(n):
    print(num1)
    num1 = num1 + num2 + num3
    num2 = num1
    num3 = num2