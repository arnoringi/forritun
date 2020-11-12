def is_prime(n):
    ''' Returns True if the given positive number is prime and False otherwise '''
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
        
# The main program starts here
# Unfinished ***