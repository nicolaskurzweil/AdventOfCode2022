points_result = { "Lost": 0, "Draw": 3, "Won": 6}
points_chosen = { "Rock": 1, "Paper": 2, "Scissors": 3}
total_score = 0

# Read Content of input file
with open("Day 2/input", "r") as f:
    rows = f.read().strip("\n").replace("A", "Rock").replace("B", "Paper").replace("C", "Scissors").replace("X", "Lose").replace("Y", "Draw").replace("Z", "Win")

# Find out what I need to play                
content = rows.replace("Rock Lose", "Rock Scissors").replace("Paper Lose", "Paper Rock").replace("Scissors Lose", "Scissors Paper").replace("Rock Draw", "Rock Rock").replace("Paper Draw", "Paper Paper").replace("Scissors Draw", "Scissors Scissors").replace("Rock Win", "Rock Paper").replace("Paper Win", "Paper Scissors").replace("Scissors Win", "Scissors Rock").split("\n")

# Calculate score
for row in content:
    total_score += points_result["Won"] + points_chosen[row.split(" ")[1]] if row == "Rock Paper" or row == "Paper Scissors" or row == "Scissors Rock" else 0
    total_score += points_result["Lost"] + points_chosen[row.split(" ")[1]] if row == "Rock Scissors" or row == "Paper Rock" or row == "Scissors Paper" else 0
    total_score += points_result["Draw"] + points_chosen[row.split(" ")[1]] if row == "Rock Rock" or row == "Paper Paper" or row == "Scissors Scissors" else 0

print(total_score)