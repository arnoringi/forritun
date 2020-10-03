# 3. Dog's age

dog_age = int(input("Input dog's age: ")) # Do not change this line

human_age_younger = 15
human_age_older = 20

if dog_age > 0 and dog_age <= 16:
    if dog_age == 1:
        print("Human age:", human_age_younger)
    else:
        for age in range(1, dog_age):
            human_age_older += 4
        print("Human age:", human_age_older)
else:
    print("Invalid age")