#PF-Assgn-41
def find_ten_substring(num_str):
    num_list = []
    subs_list = []
    
    for char in num_str:
        num_list.append(int(char))
        
    i = 0
    j = 0
    sum = 0
    
    for i in range(0, len(num_list) - 1):
        for j in range(i, len(num_list)):
            sum += num_list[j]
            if sum == 10:
                subs_list.append(num_str[i : j + 1])
            elif sum > 10:
                sum = 0
                break
            else:
                pass
    
    return subs_list    

num_str="2825302"
print("The number is:",num_str)
result_list = find_ten_substring(num_str)
print(result_list)
