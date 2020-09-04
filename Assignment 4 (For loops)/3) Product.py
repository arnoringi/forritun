first = int(input("Input the first integer: "))
second = int(input("Input the second integer: "))

count = 0
for i in range (1, second + 1):
    count += first
    
print(count)