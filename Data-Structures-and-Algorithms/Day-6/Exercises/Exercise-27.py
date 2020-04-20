#DSA-Exer-27

def find_subsequences(sequence, index, subsequence, result_list):
    # Print the subsequence when reach the leaf of recursion tree
    if index == len(sequence):
        # Condition to avoid printing empty subsequence
        if len(subsequence) != 0:
            if check_if_in_order(subsequence):
                #print("Subsequence: ", subsequence)
                result_list.append(subsequence)
    else:
        # Subsequence without including the element at current index
        find_subsequences(sequence, index + 1, subsequence, result_list)
        # Subsequence including the element at current index
        find_subsequences(sequence, index + 1, subsequence + [sequence[index]], result_list)
    return

def check_if_in_order(subsequence):
    for i in range(len(subsequence) - 1):
        if subsequence[i] >= subsequence[i + 1]:
            return False
    return True

def max_sum_is(num_list):
    result_list = []
    find_subsequences(num_list, 0, [], result_list)
    #print(result_list)
    sum_list = []
    for subsequence in result_list:
        sum_list.append(sum(subsequence))
    
    # To check the subsequences
    '''
    for i in range(0, len(result_list)):
        print(result_list[i], ' = ', sum_list[i])
    '''
    return max(sum_list)

#Pass different values to the function and test your program
num_list = [45, 78, 22, 42, 12, 3, 78]
print("Sum of the maximum sum increasing subsequence is :", max_sum_is(num_list))
