#DSA-Assgn-24
def count_decoding(digit_list):
    count = [0] * (len(digit_list) + 1)
    count[0] = 1
    count[1] = 1
  
    for i in range(2, len(digit_list) + 1): 
        count[i] = 0

        if (digit_list[i - 1] > 0):
            count[i] = count[i - 1]
  
        if (digit_list[i - 2] == 1 or (digit_list[i - 2] == 2 and digit_list[i - 1] < 7)):
            count[i] += count[i - 2] 
      
    return count[-1] 

#Pass different values to the function and test your program
digit_list = [9, 8, 1, 5]
print("Number of possible decodings for the given sequence is:", count_decoding(digit_list))
