# Read Content of input file
f = open("Day 1/input", "r")
rows = f.readlines()
f.close()

elves = [[]]

for row in rows:
    if not row.strip().isdigit():
        elves.append([])
    else:
        elves[len(elves) - 1].append(int(row.strip()))

# Calculate sum of calories
index = 0
for elf in elves:
    elves[index] = sum(elf)
    index += 1

# Get max values
elves.sort(reverse=True)
print (sum(elves[:3]))