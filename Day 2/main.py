points_result = { "Lost": 0, "Draw": 3, "Won": 6}
points_chosen = { "Rock": 1, "Paper": 2, "Scissors": 3}
total_score = 0

# Read Content of input file
with open("Day 2/input", "r") as f:
    rows = f.read().replace("A", "Rock").replace("B", "Paper").replace("C", "Scissors").replace("X", "Rock").replace("Y", "Paper").replace("Z", "Scissors").split("\n")

# Calculate score
for row in rows:
    row = row.split(" ")
    if len(row) == 2:
        if (row[1] == "Rock" and row[0] == "Scissors") or (row[1] == "Paper" and row[0] == "Rock") or (row[1] == "Scissors" and row[0] == "Paper"):
            total_score += points_result["Won"]
        elif (row[1] == "Rock" and row[0] == "Paper") or (row[1] == "Paper" and row[0] == "Scissors") or (row[1] == "Scissors" and row[0] == "Rock"):
            total_score += points_result["Lost"]
        elif (row[1] == "Rock" and row[0] == "Rock") or (row[1] == "Paper" and row[0] == "Paper") or (row[1] == "Scissors" and row[0] == "Scissors"):
            total_score += points_result["Draw"]
        total_score += points_chosen[row[1]]  

print(total_score)                