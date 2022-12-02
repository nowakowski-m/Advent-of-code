with open("day2.txt") as elfs:

    allList = [all.rstrip() for all in elfs]

your = []
enemy = []

for x in allList:
    enemy.append(x[0])
    your.append(x[2])

points = 0

#x you have to lose
#y you have to draw
#z you have to win

# X C win     X A draw    X B lose
# Y A win     Y B draw    Y C lose
# Z B win     Z C draw    Z A lose

for y in range(len(your)):

    if your[y] == "X":
        points += 0
        if enemy[y] == "A":
            points += 3
        elif enemy[y] == "B":
            points += 1
        elif enemy[y] == "C":
            points += 2

    if your[y] == "Y":
        points += 3
        if enemy[y] == "A":
            points += 1
        elif enemy[y] == "B":
            points += 2
        elif enemy[y] == "C":
            points += 3

    if your[y] == "Z":
        points += 6
        if enemy[y] == "A":
            points += 2
        elif enemy[y] == "B":
            points += 3
        elif enemy[y] == "C":
            points += 1
        
print(points)