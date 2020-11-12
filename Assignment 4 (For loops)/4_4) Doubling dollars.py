max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))
dollars = 1
days = 0

# Fill in the missing code
for i in range(1, max_days+1):
    dollars *= 2
    days += 1
    if dollars > target and days <= max_days:
        print('Days needed:',days)
        break

if dollars <= target and days <= max_days:
    print('Days needed: 0')