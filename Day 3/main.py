shared_items = []

# Read input file
with open("Day 3/input", "r") as f:
    rows = f.read().strip("\n").split("\n")

# Find shared items
for row in rows:
    for char in row[:len(row) // 2]:
        if char in row[len(row) // 2:]:
            shared_items.append(ord(char)-96 if char.islower() else ord(char)-38)
            break

print(sum(shared_items))