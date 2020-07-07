#PF-Assgn-44

def find_duplicates(list_of_numbers):
    
    duplicates = []
    
    #start writing your code here
    for i in range(0, len(list_of_numbers) - 1):
        temp_list = list_of_numbers[i + 1 : ]
        if list_of_numbers[i] in temp_list:
            if list_of_numbers[i] not in duplicates:
                duplicates.append(list_of_numbers[i])
                
    return duplicates

list_of_numbers = [12,54,68,759,24,15,12,68,987,758,25,69]
list_of_duplicates = find_duplicates(list_of_numbers)
print(list_of_duplicates)
