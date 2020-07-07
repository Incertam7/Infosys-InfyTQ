#PF-Assgn-43

def find_factors(num):
    factors = []
    temp = num
    
    while temp > 0:
        if num % temp == 0:
            factors.append(temp)
        temp -= 1
        
    return factors
    
def count_factors(num):
    return len(find_factors(num))

def find_smallest_number(num):
    temp = 0
    
    while True:
        if count_factors(temp) == num:
            return temp
        else:
            temp += 1

num = 16
find_factors(16)
print("The number of divisors :", num)
result = find_smallest_number(num)
print("The smallest number having", num, " divisors:", result)
