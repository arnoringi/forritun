# Project 3: Fibo and abundant

type_sequence = input("Input f|a|b (fibonacci, abundant or both): ")

### Fibonacci Sequence
if type_sequence == 'f' or type_sequence == 'b':
    
    length = int(input("Input the length of the sequence: "))

    print("Fibonacci Sequence:")
    print("-------------------")

    # These variables are meant for the start of the sequence
    num1 = 0
    num2 = 1
    sum_int = 0
    print(num1)
    print(num2)

    # The sum adds the most recent numbers (num1, num2) together, then changes them
    for i in range(2, length):
        sum_int = num1 + num2
        print(sum_int)
        num1 = num2
        num2 = sum_int

### Abundant numbers
if type_sequence == 'a' or type_sequence == 'b':
    
    max_num = int(input("Input the max number to check: "))

    print("Abundant numbers:")
    print("-----------------")

    sum_int = 0

    # The i for loop checks if number n is an abundant number
    for i in range(1, max_num+1):
        for j in range (1, i): # The j for loop checks all numbers that are proper divisors for number i
            # If number can be divided with number j, then add to sum
            if i % j == 0: 
                sum_int += j
            
            # If sum is bigger than number, then print
            if sum_int > i:
                print(i)
                sum_int = 0
                break
            
            # Sum reset
            if j == (i - 1):
                sum_int = 0



### ALGRÍM ###
# Fibonacci
    # Fyrstu tvær tölurnar eru 0 og 1
    # Næstu tölur eftir það eru summa næstu tveggja á undan (0, 1, 1, 2, 3, 5, 8, 13...)
    # Tala n á að vera >= 2

    # 1. Ef input er 'f' EÐA 'b' þá keyrir þetta
    # 2. Input length segir til um hversu margar tölur á að prenta
    # 3. Prentar "Fibonacci Sequence:" og svo "-------------------" í annari línu
    # 4. Byrja á að prenta 0 og 1
    # 5. For loopa 2, n mörgum sinnum
    # 6. Í hverju loopi skal bæta saman seinustu tveim tölum

# Abundant
    # Summa allra talna sem gengur upp í n töluna er hærri en n talan sjálf
    # Summan eru allar tölurnar nema n talan

    # 1. Ef input er 'a' EÐA 'b' þá keyrir þetta
    # 2. Input max number til að gá hvaða tölur eru abundant
    # 3. Prentar "Abundant numbers:" og svo "-------------------" í annari línu
    # 4. Gera for loop fyrir tölurnar sem á að tjékka
    # 5. Gera nested for loop til að tjékka hvaða tölur ganga upp í töluna