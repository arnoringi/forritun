# is_prime function definition goes here
def is_prime(num):
    prime = False
    for i in range (2, num):
        if (num % i) == 0:
            break
    else:
        prime = True
    return prime
    
max_num = int(input("Input an integer greater than 1: "))

# Call the function here repeatadly from 2 to max_num and print out the appropriate message
for i in range(2, max_num+1):
    if is_prime(i) == False:
        print(i, "is not a prime")
    else:
        print(i, "is a prime")