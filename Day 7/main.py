# Read input file
with open("Day 7/input.txt", "r") as f:
    input = f.read().strip("\n").splitlines()

disc: object = {}

# Parse input
current_dir = "/home"
for i, line in enumerate(input):
    if "$ cd .." in line:
        current_dir = current_dir[:current_dir.rindex("/")]
    elif "$ cd " in line:
        current_dir += "/" + line.split(" ")[2] if "$ cd /" not in line else ""
        disc[current_dir] = 0
        # Check the following lines until a new directory is opened
        for following_line in input[i+2:]:
            if "$" in following_line: break
            if "dir" not in following_line:
                disc[current_dir] += int(following_line.split(" ")[0])

for name_of_dir,value_of_dir in disc.items():
    # Check if the directory has children, if so, sum up the size of the children
    for name_of_dir_two,value_of_dir_two in disc.items():
        if name_of_dir + "/" in name_of_dir_two:
            value_of_dir += value_of_dir_two  
    disc[name_of_dir] = value_of_dir          

# Sum up directories with size maximum 100000
sum = 0
for name_of_dir,value_of_dir in disc.items():
    sum += value_of_dir if value_of_dir <= 100000 else 0

# Print result
print(sum)