#DSA-Tryout

import random

def find_it(num, element_list):
    no_of_guesses = 0
    for number in element_list:
        no_of_guesses += 1
        if number == num:
            print("Success")
            break
        else:
            print("Try again")
    print("Guessed in", no_of_guesses, "tries")

#Initializes a list with values 1 to n in random order and returns it
def initialize_list_of_elements(n):
    list_of_elements = []
    for i in range(1, n + 1):
        list_of_elements.append(i)
    mid = n // 2
    for j in range(0, n):
        index1 = random.randrange(0, mid)
        index2 = random.randrange(mid, n)
        num1 = list_of_elements[index1]
        list_of_elements[index1] = list_of_elements[index2]
        list_of_elements[index2] = num1
    return list_of_elements

def play(n):
    num_list = initialize_list_of_elements(n)
    number_to_be_guessed = random.randrange(0, n + 1)
    find_it(number_to_be_guessed, num_list)

#Pass different values to play() and observe the output
play(400)
