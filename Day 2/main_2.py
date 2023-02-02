points_lost = 0
points_draw = 3
points_won = 6
chose_rock = 1 # A = Rock
chose_paper = 2 # B = Paper
chose_scissors = 3 # C = Scissors

total_score = 0

# Read Content of input file
with open("Day 2/input", "r") as f:
    rows = f.readlines()

# X=lose, Y=draw, Z=win
# Find out what I need to play
content = []    
for row in rows:
    temp = row.replace("A", "Rock").replace("B", "Paper").replace("C", "Scissors").replace("X", "Lose").replace("Y", "Draw").replace("Z", "Win").replace("\n", "")
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
    if row[1] == "Rock":
       if row[0] == "Scissors":
           total_score += points_won
       elif row[0] == "Paper":
           total_score += points_lost
       else:
           total_score += points_draw    
       total_score += chose_rock    
    elif row[1] == "Paper":
        if row[0] == "Rock":
            total_score += points_won
        elif row[0] == "Scissors":
            total_score += points_lost
        else:
            total_score += points_draw
        total_score += chose_paper       
    elif row[1] == "Scissors":
        if row[0] == "Paper":
            total_score += points_won
        elif row[0] == "Rock":
            total_score += points_lost    
        else:
            total_score += points_draw
        total_score += chose_scissors

print(total_score)                