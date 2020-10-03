my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
quotient = my_int
remainder = 0
bin_str = ''

for index in range(7):
    remainder = quotient % 2
    quotient = quotient // 2
    if remainder == 0:
        bin_str = bin_str + '0'
    else:
        bin_str = bin_str + '1'

bin_str = bin_str[::-1]
print("The binary of {} is {}".format(my_int,bin_str))