#DSA-Assgn-19

def last_instance(num_list, start, end, key):
    index = -1
    
    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] == key:
            index = mid
            #print(key, "found at position", index)
            break
        elif num_list[mid] > key:
            end = mid - 1
        elif num_list[mid] < key:
            start = mid + 1
    
    if index > -1:
        for i in range(index + 1, len(num_list)):
            if num_list[i] == key:
                index = i
            else:
                break
            
    return index

num_list = [10, 11, 12, 12, 13]
start = 0
end = len(num_list) - 1
key = 11 #Number to be searched
#Pass different values for num_list, start, end and key and test your program
result = last_instance(num_list, start, end, key)

if(result != -1):
    print("The index position of the last occurrence of the number:", result)
else:
    print("Number not found")
