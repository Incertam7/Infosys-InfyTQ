#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    num_list.sort()
    
    pairs = 0
    
    for i in range(0, len(num_list) - 1):
    
        if num_list[i] == n or num_list[i] > n:
            return 0
        else:
            for j in range(i + 1, len(num_list)):
                if (num_list[i] + num_list[j]) == n:
                    pairs += 1
                    
    return pairs

num_list = [4, 6, 1, 5, 2]
n = 7
print(find_pairs_of_numbers(num_list,n))
