rating = int(input("Input elo rating: ")) # Do not change this line
# Fill in the missing code below
if rating > 999:
    if rating >= 2700:
        print("Super grandmaster")
    elif rating < 2700 and rating >= 2500:
        print("Grandmaster")
    elif rating < 2500 and rating >= 2400:
        print("International")
    elif rating < 2400:
        print("Amateur")
else:
    print("Invalid")