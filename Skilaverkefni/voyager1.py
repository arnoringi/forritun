days = int(input("Number of days after 9/25/09: "))

# The following numbers are in miles
miles_sep2009 = 16637000000
distance_p_hour = 38241
distance_p_day = distance_p_hour * 24

miles_traveled = miles_sep2009 + (distance_p_day * days)
km_traveled = round(miles_traveled * 1.609344) # 1 mile is 1.609344 km
au_traveled = round(miles_traveled / 92955887.6) # 1 AU is 92955887.6 miles

print("Miles from the sun:", miles_traveled)
print("Kilometers from the sun:", km_traveled)
print("AU from the sun:", au_traveled)