#Disclaimer: this program only works for when entering valid digits

#Valid digits:
#1) Letters A - Z
#2) Numbers 0 - 9
#3) Special characters: (see constant SPECIAL below)

#Constants (int / str)
PASSWORD_MIN = 6
PASSWORD_MAX = 20
SPECIAL = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

#Password counters (int)
valid = 0
invalid = 0
password_count = 0

#Character counters (int)
char_lower = 0
char_upper = 0
char_number = 0

#Which password condition(s) is/are missing, if any (str)
password_conditions = ""

##########################################
password = input("Enter a new password: ")

while password != 'q':
    if len(password) >= PASSWORD_MIN and len(password) <= PASSWORD_MAX:
        #Removing special characters
        for char in password:
            for digits in SPECIAL:
                if char == digits:
                    password = password.replace(char, "")

        #Character counters
        for char in password:
            if char.isdigit():
                char_number += 1
            elif char == char.lower():
                char_lower += 1
            elif char == char.upper(): #This is elif in case an invalid character somehow gets through
                char_upper += 1
        
        #Condition check (It is possible to change these values depending on how many should be required)
        if char_lower >= 1: #Lower-case check
            password_conditions += 'T'
        else:
            password_conditions += 'F'
        
        if char_upper >= 1: #Upper-case check
            password_conditions += 'T'
        else:
            password_conditions += 'F'
        
        if char_number >= 1: #Number check
            password_conditions += 'T'
        else:
            password_conditions += 'F'
        
        #Condition display
        if password_conditions == "TTT": #All conditions are fufilled
            print("Valid password of length {}".format(len(password)))
            valid += 1
            password_count += 1
        else: #Check which conditions are missing
            #Lower-case check (T/F)
            if password_conditions[0] == 'F':
                print("At least one lower case letter needed")
            #Upper-case check (T/F)
            if password_conditions[1] == 'F':
                print("At least one upper case letter needed")
            #Number check (T/F)
            if password_conditions[2] == 'F':
                print("At least one number needed")
            invalid += 1
            password_count += 1
        
        #Character reset
        char_lower = 0
        char_upper = 0
        char_number = 0

        #Condition reset
        password_conditions = ""
    else:
        print("Invalid length")
        invalid += 1
        password_count += 1
    password = input("Enter a new password: ")

print("You tried {} passwords, {} valid, {} invalid".format(password_count, valid, invalid))