with open("day2.txt") as elfs:

    allList = [all.rstrip() for all in elfs]

your = []
enemy = []

for x in allList:
    enemy.append(x[0])
    your.append(x[2])

points = 0

# X C win     X A draw    X B lose
# Y A win     Y B draw    Y C lose
# Z B win     Z C draw    Z A lose

for y in range(0, len(your)):
    if your[y] == "X":
        points += 1
        if enemy[y] == "C":
            points += 6
        elif enemy[y] == "A":
            points += 3
        elif enemy[y] == "B":
            points += 0
    if your[y] == "Y":
        points += 2
        if enemy[y] == "A":
            points += 6
        elif enemy[y] == "B":
            points += 3
        elif enemy[y] == "C":
            points += 0
    if your[y] == "Z":
        points += 3
        if enemy[y] == "B":
            points += 6
        if enemy[y] == "C":
            points += 3
        if enemy[y] == "A":
            points += 0
        
print(points)