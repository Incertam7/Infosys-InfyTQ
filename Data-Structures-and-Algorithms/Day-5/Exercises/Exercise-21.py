#DSA-Exer-21

def merge_sort(num_list):
    low = 0
    high = len(num_list) - 1
    if low == high:
        return num_list
    else:
        left_list = num_list[0 : (low + high) // 2 + 1]
        right_list = num_list[(low + high) // 2 + 1 : high + 1]
        return merge(merge_sort(left_list), merge_sort(right_list))

def merge(left_list, right_list):
    i = j = 0
    merged_list = []
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            j += 1
    
    while i < len(left_list):
        merged_list.append(left_list[i])
        i += 1
        
    while j < len(right_list):
        merged_list.append(right_list[j])
        j += 1
        
    return merged_list

num_list = [34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:", num_list)
sorted_list = merge_sort(num_list)
print("After sorting:", sorted_list)
