#PF-Assgn-38

def check_double(number):
    doubled = number * 2
    
    same_len = False
    same_digits = False
    
    if(len(str(doubled)) == len(str(number))):
        same_len = True
        
    if same_len:
        for num in str(doubled):
            if num not in str(number):
                return False
            else:
                same_digits = True
    else:
        return False
        
    if same_digits:
        return True

#Provide different values for number and test your program
print(check_double(142857))
