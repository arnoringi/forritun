# 5. Pattern

max_int = int(input("Input max integer: "))
num = 0

for i in range(1, max_int+1):
    for j in range(i):
        num += 1
        print(num, end=' ')
    print()
    num = 0