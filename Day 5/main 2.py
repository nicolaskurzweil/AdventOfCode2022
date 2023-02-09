# Read input file
with open("Day 5/input.txt", "r") as f:
    rows = f.read().strip("\n").split("\n\n")

temp_stacks = rows[0].strip("\n")
rules = rows[1].strip("\n").strip(" ").split("\n")

# Create stacks
stacks: dict[int, list] = {}
for stack in range(1, int(temp_stacks.strip(" ")[-1])+1):
    stacks[stack] = []

temp_stacks = temp_stacks.split("\n")
temp_stacks.pop()

for stack in stacks.items():
    move_to_right = (int(stack[0]) - 1) * 4
    for row in temp_stacks:
        if row[move_to_right:move_to_right+3] != "   ":
            stacks[stack[0]].append(row[move_to_right:move_to_right+3].replace("[", "").replace("]", ""))

# Apply rules
for rule in rules:
    amount = int(rule.split(" ")[1])
    origin = int(rule.split(" ")[3])
    destination = int(rule.split(" ")[5])

    for i in range(1, amount+1):
        stacks[destination].insert(0, stacks[origin].pop(0 + amount - i))  

# Print result
result = ""
for stack in stacks.values():
    result = result + stack[0]
print(result)