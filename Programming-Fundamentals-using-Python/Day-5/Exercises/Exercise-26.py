#PF-Exer-26

def factorial(number):
    fact = 1
    while number > 0:
        fact *= number
        number -= 1
        
    return fact

def find_strong_numbers(num_list):
    
    strong_list = []
    
    for num in num_list:
        sum = 0
        
        if num == 0:
            sum = 1

        temp = num
        
        while temp > 0:
            rem = temp % 10
            rem_fact = factorial(rem)
            sum += rem_fact
            temp //= 10
        
        if sum == num:
            strong_list.append(num)
            
    return strong_list

num_list=[145, 2, 10, 0]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
