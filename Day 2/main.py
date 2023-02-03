points_result = { "Lost": 0, "Draw": 3, "Won": 6}
points_chosen = { "Rock": 1, "Paper": 2, "Scissors": 3}
total_score = 0

# Read Content of input file
with open("Day 2/input", "r") as f:
    rows = f.read().replace("A", "Rock").replace("B", "Paper").replace("C", "Scissors").replace("X", "Rock").replace("Y", "Paper").replace("Z", "Scissors").split("\n")

# Calculate score
for row in rows:
    if len(row.split(" ")) == 2:
        if row == "Scissors Rock" or row == "Rock Paper" or row == "Paper Scissors":
            total_score += points_result["Won"]
        elif row == "Rock Scissors" or row == "Paper Rock" or row == "Scissors Paper":
            total_score += points_result["Lost"]
        elif row == "Rock Rock" or row == "Paper Paper" or row == "Scissors Scissors":
            total_score += points_result["Draw"]
        total_score += points_chosen[row.split(" ")[1]] 

print(total_score)