#DSA-Tryout

import random
from timeit import default_timer as timer

def find_it_binary(num, element_list):
    no_of_guesses = 0
    low = 0
    high = len(element_list) - 1
    while low < high:
        no_of_guesses += 1
        mid = (low + high) // 2
        if element_list[mid] == num:
            #print("Success")
            break
        elif element_list[mid] > num:
            high = mid - 1
        else:
            low = mid + 1
            
    return no_of_guesses
    #print("Guessed in", no_of_guesses, "tries")

def find_it_linear(num, element_list):
    no_of_guesses = 0
    for number in element_list:
        no_of_guesses += 1
        if number == num:
            #print("Success")
            break
        else:
            pass
    return no_of_guesses
    #print("Guessed in", no_of_guesses, "tries")

#Initializes a list with values 1 to n in random order and returns it
def initialize_list_of_elements(n, ascending = True):
    list_of_elements = []
    if ascending:
        for i in range(1, n + 1):
            list_of_elements.append(i)
    else:
        for i in range(n, 0, -1):
            list_of_elements.append(i)
    return list_of_elements

def play(n):
    list_of_elements = initialize_list_of_elements(n)
    rand_index = random.randrange(0, len(list_of_elements))
    rand_num = list_of_elements[rand_index]
    print("Range:", n)
    print("Number to be guessed:", rand_num)
    start = timer()
    print("No. of guesses made using linear search:", find_it_linear(rand_num, list_of_elements))
    end = timer()
    print("Linear Search:Execution time in seconds:{0:.5f}".format((end-start)))
    start = timer()
    print("No. of guesses made using binary search:", find_it_binary(rand_num, list_of_elements))
    end = timer()
    print("Binary Search:Execution time in seconds:{0:.5f}".format((end-start)))

#Pass different values to play() and observe the output
play(100)
print()
play(1000)
print()
play(10000)
print()
play(100000)
print()
play(1000000)
