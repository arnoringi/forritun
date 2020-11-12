def valid_date(date):
    is_true = False
    conditions = 0 #The conditions must reach 5 for the date to become valid 
    count = 0
    
    #Condition 0 (Intiger check)
    for turn in range(8):
        if turn == 2 or turn == 5:
            pass
        elif date[turn].isdigit():
                count += 1
    if count == 6:
        count = 0

        #Condition 1 (8 digits)
        for digits in date:
            count += 1
        if count == 8:
            conditions += 1

        #Condition 2 (Period seperator)
        if date[2] == '.' and date[5] == '.':
            conditions += 1
        
        #Condition 3 (Day between 01 and 31)
        if int(date[1]) >= 1 and int(date[1]) <= 9 and date[0] == '0': #Day 01 - 09
            conditions += 1
        elif int(date[:2]) >= 10 and int(date[:2]) <= 31: #Day 10 - 31
            conditions += 1
        
        #Condition 4 (Month between 01 and 12)
        if int(date[4]) >= 1 and int(date[4]) <= 9 and date[3] == '0': #Month 01 - 09
            conditions += 1
        elif int(date[3:5]) >= 10 and int(date[3:5]) <= 12: #Month 10 - 12
            conditions += 1
        
        #Condition 5 (Year between 00 and 99)
        if int(date[7]) >= 0 and int(date[7]) <= 9 and date[6] == '0': #Year 00-09
            conditions += 1
        elif int(date[6:8]) >= 10 and int(date[6:8]) <= 99: #Year 10 - 99
            conditions += 1
        
        #Condition check
        if conditions == 5:
            is_true = True
    
    return is_true

date_str = input("Enter a date: ")

if valid_date(date_str):
    print("Date is valid")
else:
    print("Date is invalid")