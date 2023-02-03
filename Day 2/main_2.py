points_result = { "Lost": 0, "Draw": 3, "Won": 6}
points_chosen = { "Rock": 1, "Paper": 2, "Scissors": 3}
total_score = 0

# Read Content of input file
with open("Day 2/input", "r") as f:
    rows = f.readlines()

# Find out what I need to play
content = []    
for row in rows:
    temp = row.replace("A", "Rock").replace("B", "Paper").replace("C", "Scissors").replace("X", "Lose").replace("Y", "Draw").replace("Z", "Win").strip()
    print(temp)
    if "Lose" in temp and "Rock" in temp:
        temp = temp.replace("Lose", "Scissors")
    elif "Lose" in temp and "Paper" in temp:
        temp = temp.replace("Lose", "Rock")
    elif "Lose" in temp and "Scissors" in temp:
        temp = temp.replace("Lose", "Paper")
    elif "Draw" in temp and "Rock" in temp:
        temp = temp.replace("Draw", "Rock")
    elif "Draw" in temp and "Paper" in temp:
        temp = temp.replace("Draw", "Paper")
    elif "Draw" in temp and "Scissors" in temp:
        temp = temp.replace("Draw", "Scissors")
    elif "Win" in temp and "Rock" in temp:
        temp = temp.replace("Win", "Paper")
    elif "Win" in temp and "Paper" in temp:
        temp = temp.replace("Win", "Scissors")
    elif "Win" in temp and "Scissors" in temp:
        temp = temp.replace("Win", "Rock") 
    content.append(temp)                  

# Calculate score
for row in content:
    row = row.split(" ")
    if (row[1] == "Rock" and row[0] == "Scissors") or (row[1] == "Paper" and row[0] == "Rock") or (row[1] == "Scissors" and row[0] == "Paper"):
        total_score += points_result["Won"]
    elif (row[1] == "Rock" and row[0] == "Paper") or (row[1] == "Paper" and row[0] == "Scissors") or (row[1] == "Scissors" and row[0] == "Rock"):
        total_score += points_result["Lost"]
    elif (row[1] == "Rock" and row[0] == "Rock") or (row[1] == "Paper" and row[0] == "Paper") or (row[1] == "Scissors" and row[0] == "Scissors"):
        total_score += points_result["Draw"]
    total_score += points_chosen[row[1]]            

print(total_score)                