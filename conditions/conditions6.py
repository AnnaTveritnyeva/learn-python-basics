team_A_score = int(input("Please enter team A score: \n"))
team_B_score = int(input("Please enter team B score: \n"))

if team_A_score == team_B_score:
    print("draw")
elif team_A_score > team_B_score:
    print("Team A won!")
else:
    print("Team B won!")
