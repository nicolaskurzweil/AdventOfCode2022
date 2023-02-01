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
for elf in elves:
    if sum(elf) > max_calories:
        max_calories = sum(elf)

print("Maximum calories: " + str(max_calories))