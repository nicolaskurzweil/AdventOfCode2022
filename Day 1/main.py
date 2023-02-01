# Read Content of input file
with open("Day 1/input", "r") as f:
  rows = f.read()
elves = rows.split("\n\n")

# Calculate sum of calories
for elf in elves:
    elves[elves.index(elf)] = sum(list(map(int, elf.split("\n"))))

# Get max values
elves.sort(reverse=True)
print (sum(elves[:3]))