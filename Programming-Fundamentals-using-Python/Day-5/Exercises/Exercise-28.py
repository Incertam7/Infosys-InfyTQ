#PF-Exer-28
                                              
#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    team1_wins = 0
    team2_wins = 0
    
    for team in match_tuple:
        if team == "Team1":
            team1_wins += 1
        elif team == "Team2":
            team2_wins += 1
        else:
            print("Invalid team name.")
            
    if team1_wins > team2_wins:
        return "Team1"
    elif team2_wins > team1_wins:
        return "Team2"
    else:
        return "Tie"

#Invoke the function with each of the print statements given below
print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))
#print(find_winner_of_the_day("Team1","Team2","Team1","Team2"))
