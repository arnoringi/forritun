name = input("Input a name: ")

lastname, first_name = name.split()

#Til að eyða kommunni
for char in lastname:
    if char == ',':
        lastname = lastname.replace(char, "")

first_inital = first_name[0].capitalize()
lastname = lastname.capitalize()

print(first_inital + ". " + lastname)