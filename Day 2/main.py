points_lost = 0
points_draw = 3
points_won = 6

chose_rock = 1 # A/X = Rock
chose_paper = 2 # B/Y = Paper
chose_scissors = 3 # C/Z = Scissors

total_score = 0

# Read Content of input file
with open("Day 2/input", "r") as f:
    rows = f.read().replace("A", "Rock").replace("B", "Paper").replace("C", "Scissors").replace("X", "Rock").replace("Y", "Paper").replace("Z", "Scissors").split("\n")

# Calculate score
for row in rows:
    row = row.split(" ")
    if len(row) == 2:
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