print("Welcome to car rentals!")

while True:
    yes_or_no = input("Would you like to continue (y/n)? ")
    if yes_or_no == 'y':
        cc = input("Customer code (b or d): ")
        
        if cc == 'b': # User has selected option 'budget'
            # Rates for option 'budget'
            base_rate = float(40)
            mile_rate = float(0.25)

            # User inputs info
            days = int(input("Number of days: "))
            miles_start = int(input("Odometer reading at the start: "))
            miles_end = int(input("Odometer reading at the end: "))

            # Mile calculation
            miles_total = miles_end - miles_start
            print("Miles driven:", miles_total)

            # Cost calculation
            total_cost = float((base_rate * days) + (miles_total * mile_rate))
            print("Amount due:", round(total_cost, 1))
        else: # User has selected option 'daily'
            # Rates for option 'daily'
            base_rate = float(60)
            mile_rate = float(0.25) # Only if user has driven more than 100 miles per day

            # User inputs info
            days = int(input("Number of days: "))
            miles_start = int(input("Odometer reading at the start: "))
            miles_end = int(input("Odometer reading at the end: "))

            # Mile and cost calculation
            miles_total = (miles_end - miles_start) - (days * 100)
            if miles_total > 0: # If miles are more than 100 per day
                total_cost = float((days * base_rate) + (miles_total * mile_rate))
                miles_total = miles_end - miles_start
            else: # If miles are less than 100 per day
                miles_total = miles_end - miles_start 
                total_cost = float(days * base_rate)
            print("Miles driven:", miles_total)
            print("Amount due:", round(total_cost, 1))
    else:
        break