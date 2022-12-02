with open("day1.txt") as elfs:

    elfsCalories = elfs.readlines()

caloriesList = list(elfsCalories)

elfsList = []
z = 0

for x in caloriesList:
    if x == "\n":
        elfsList.append(z)
        z = 0
    else:
        z += int(x)

print(max(elfsList))