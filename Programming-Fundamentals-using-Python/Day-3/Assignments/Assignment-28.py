#PF-Assgn-28

def find_max(num1, num2):
    max_num = -1
    # Write your logic here
    if(num1 >= num2):
        return max_num
    
    list = []
    
    for num in range(num1, num2 + 1):
        if multiple_of_five(num) and two_digits(num) and sum_of_digits_multi_3(num):
            list.append(num)
            
    if len(list) > 0:
        max_num = list[len(list) - 1]

    return max_num
    
def multiple_of_five(num):
    if num % 5 == 0:
        return True
    else:
        return False
        
def two_digits(num):
    if num >= 10 and num < 100:
        return True
    else:
        return False

def sum_of_digits_multi_3(num):
    if num % 3 == 0:
        return True
    else:
        return False

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10, 15)
print(max_num)
