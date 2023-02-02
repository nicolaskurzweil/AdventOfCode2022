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
    points_round = 0
    row = row.split(" ")
    if len(row) == 2:
        if row[1] == "Rock":
            if row[0] == "Scissors":
                points_round += points_won
            elif row[0] == "Paper":
                points_round += points_lost
            else:
                points_round += points_draw    
            points_round += chose_rock    
        elif row[1] == "Paper":
            if row[0] == "Rock":
                points_round += points_won
            elif row[0] == "Scissors":
                points_round += points_lost
            else:
                points_round += points_draw
            points_round += chose_paper       
        elif row[1] == "Scissors":
            if row[0] == "Paper":
                points_round += points_won
            elif row[0] == "Rock":
                points_round += points_lost    
            else:
                points_round += points_draw
            points_round += chose_scissors

        total_score += points_round 

print(total_score)                