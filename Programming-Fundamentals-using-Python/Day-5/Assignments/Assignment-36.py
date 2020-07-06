#PF-Assgn-36
def create_largest_number(number_list):
    number_list.sort(reverse = True)
    
    largest_number = 0
    
    for num in number_list:
        largest_number = largest_number * 100 + num

    return largest_number
    
number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
