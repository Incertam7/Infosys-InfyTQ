#DSA-Assgn-17

def find_matches(country_name):
    match_detail_list = []
    for match in match_list:
        match_details = match.split(":")
        if match_details[0] == country_name:
            match_detail_list.append(match)
            
    return match_detail_list

def max_wins():
    output_dict = {}
    wins_dict = {}

    for match in match_list:
        match_details = match.split(":")
        if match_details[1] not in output_dict:
            output_dict[match_details[1]] = None
            wins_dict[match_details[1]] = None
            
        if wins_dict[match_details[1]] is None:
            output_dict[match_details[1]] = [match_details[0]]
            wins_dict[match_details[1]] = match_details[3]
        
        elif wins_dict[match_details[1]] < match_details[3]:
            output_dict[match_details[1]] = [match_details[0]]
            wins_dict[match_details[1]] = match_details[3]
            
        elif wins_dict[match_details[1]] == match_details[3]:
            output_dict[match_details[1]].append(match_details[0])
        
    print (output_dict)
    return output_dict

def find_winner(country1, country2):
    wins1 = 0
    wins2 = 0
    for match in match_list:
        match_details = match.split(":")
        if match_details[0] == country1:
            wins1 += int(match_details[3])
        elif match_details[0] == country2:
            wins2 += int(match_details[3])
    
    if wins1 > wins2:
        return country1
    elif wins2 > wins1:
        return country2
    else:
        return "Tie"
    
#Consider match_list to be a global variable
match_list = ['AUS:T20:5:3', 'IND:CHAM:5:3', 'AUS:WOR:2:0', 'CAN:CHAM:5:1', 'ENG:WOR:2:0', 'IND:T20:6:4', 'PAK:T20:4:3', 'IND:WOR:5:3', 'AUS:CHAM:1:0', 'PAK:CHAM:5:1', 'SA:CHAM:5:2', 'SA:T20:5:0', 'PAK:WOR:2:0']
#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
max_wins()
print()
