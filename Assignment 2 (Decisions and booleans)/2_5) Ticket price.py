age = int(input("Input age: ")) # Do not change this line
ticket = float(40)

if age >= 65:
    price = ticket * 0.6 # 40%
    float(print(price))
elif age < 65 and age >= 20:
    price = ticket
    float(print(price))
elif age < 20 and age > 5:
    price = ticket * 0.8 # 20%
    float(print(price))
else:
    price = 0.0
    print(price)