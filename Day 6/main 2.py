# Read input file
with open("Day 6/input", "r") as f:
    input = f.read().strip("\n")

possible_marker = ""

for char in input:
    possible_marker = possible_marker.split(char)[1] + char if char in possible_marker else possible_marker + char
    if len(possible_marker) == 14: break       
        
print(input.index(possible_marker) + 14)