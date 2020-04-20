#DSA-Tryout

import sys

sys.setrecursionlimit(10000)   #This is to overcome default python recursion limit

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    
    if num in memo:
        return memo[num]
    else:
        value = fibonacci(num - 1) + fibonacci(num - 2)
        memo[num] = value
        return value

memo={} #global dictionary to store the fibonacci number already computed
print("Fibonacci number:", fibonacci(55))
