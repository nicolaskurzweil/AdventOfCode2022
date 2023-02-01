# Read Content of input file
f = open("Day 1/input", "r")
rows = f.readlines()

elves = [[]]

for row in rows:
    if not row.strip().isdigit():
        elves.append([])
    else:
        elves[len(elves) - 1].append(int(row.strip()))

# Calculate maximum calories
max_calories = 0
second_max_calories = 0
third_max_calories = 0

for elf in elves:
    if sum(elf) > max_calories:
        third_max_calories = second_max_calories
        second_max_calories = max_calories
        max_calories = sum(elf)

print("Calories of the three max Elfes: " + str(max_calories + second_max_calories + third_max_calories))