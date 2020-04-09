#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data = ""
    words_list = []
    
    for i in range(0, len(list1)):
        temp_word = None
        if list1[i] is not None:
            temp_word = list1[i]
            if list2[-(i + 1)] is not None:
                temp_word += list2[-(i + 1)]
        else:
            if list2[-(i + 1)] is not None:
                temp_word = list2[-(i + 1)]
        
        if temp_word is not None:
            words_list.append(temp_word)
        
    merged_data = " ".join(words_list)
    
    return merged_data

#Provide different values for the variables and test your program
list1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2 = ['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']
merged_data = merge_list(list1,list2)
print(merged_data)
