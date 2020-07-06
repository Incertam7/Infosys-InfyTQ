#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    average = sum(list_of_marks) / len(list_of_marks)
    
    more_than_average = 0
    
    for mark in list_of_marks:
        if mark > average:
            more_than_average += 1
    
    return more_than_average / len(list_of_marks) * 100

def sort_marks():
    return sorted(list(list_of_marks))

def generate_frequency():
    freq_list = []
    
    for i in range(0, 26):
        freq_list.append(list_of_marks.count(i))
        
    return freq_list

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
