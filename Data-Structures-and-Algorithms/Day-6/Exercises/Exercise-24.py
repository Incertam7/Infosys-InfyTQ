#DSA-Exer-24

def make_change(denomination_list, amount):
    if amount in denomination_list:
        return 1
        
    denomination_list.sort(reverse = True)
    
    total = 0
    no_of_denominations = 0
    
    for denomination in denomination_list:
        while True:
            if denomination + total <= amount:
                total += denomination
                no_of_denominations += 1
            else:
                break
            
    if total != amount:
        return -1

    return no_of_denominations


#Pass different values to the function and test your program
amount = 20
denomination_list = [1,15,10]
print(make_change(denomination_list, amount))
