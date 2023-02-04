# Read input file
with open("Day 4/input", "r") as f:
    rows = f.read().strip("\n").split("\n")

counter = 0    

for row in rows:
    elves = row.split(",")
    elf_one = list(map(int, elves[0].split("-")))
    elf_two = list(map(int, elves[1].split("-")))
    if (elf_one[0] <= elf_two[0] and elf_one[1] >= elf_two[0]) or (elf_two[0] <= elf_one[0] and elf_two[1] >= elf_one[0]):
        counter += 1

print(counter)