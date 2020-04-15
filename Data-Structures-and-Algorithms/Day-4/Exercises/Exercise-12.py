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
    num_list = initialize_list_of_elements(n, False)
    print(num_list)
    number_to_be_guessed = random.randrange(0, n + 1)
    find_it(number_to_be_guessed, num_list)

#Pass different values to play() and observe the output
play(10)
