shared_items = []
group = []

# Read input file
with open("Day 3/input", "r") as f:
    rows = f.read().strip("\n").split("\n")

# Make groups of 3
for row in rows:
    group.append(row)
    if len(group) == 3:
        # Find shared items
        for char in group[0]:
            if char in group[1] and char in group[2]:
                shared_items.append(ord(char)-96 if char.islower() else ord(char)-38)
                break
        group = []

print(sum(shared_items))