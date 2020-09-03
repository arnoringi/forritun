#THIS IS A TEST UPLOAD

# Here are numbers
days = 0
miles = 0
total_cost = float(0)

# User selects 'y' (yes) or 'n' (no)
yes = 'y'
no = 'n'

# User selects either option 'b' (budget), or option 'd' (daily)
b = 'b'
d = 'd'

yes_or_no = input("Do you want to continue?: ")

while yes_or_no == yes:
    print("Customer classification code: 'b' (budget) or 'd' (daily)")
    option = input("Please select either option: ")
    if option == b:
        print("You have selected option 'budget'!")
        # Rates for option 'budget'
        base_rate = float(40)
        mile_rate = float(0.25)

        days = int(input("Total number of days: "))
        miles_start = int(input("Mile status at the start: "))
        miles_end = int(input("Mile status at the end: "))

        miles_total = miles_end - miles_start
        total_cost = float((days * base_rate) + (miles_total * mile_rate))
        print("Your total cost is:", total_cost, "dollars.")
        break
    elif option == d:
        print("You have selected option 'daily'!")
        # Rates for option 'budget'
        base_rate = float(60)
        mile_rate = float(0.25)

        days = int(input("Total number of days: "))
        miles_start = int(input("Mile status at the start: "))
        miles_end = int(input("Mile status at the end: "))

        # No rate is charged if miles are under 100 per day
        miles_total = (miles_end - miles_start) - (days * 100)
        if miles_total > 0:
            total_cost = float((days * base_rate) + (miles_total * mile_rate))
        else:
            total_cost = float(days * base_rate)
        print("Your total cost is:", total_cost, "dollars.")
        break
    else:
        print("Please enter a valid input.")