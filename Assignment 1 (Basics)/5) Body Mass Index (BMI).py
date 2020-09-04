weight_str = input("Weight (kg): ") # do not change this line
height_str = input("Height (cm): ") # do not change this line

weight_str = float(weight_str)
height_str = float(height_str)

height_str = height_str / 100

bmi = weight_str / height_str**2

print("BMI is: ", bmi) # do not change this line