#PF-Assgn-15

def find_product(num1, num2, num3):
    product = 0
    #write your logic here
    if(num1 == 7):
        num1 = 1
    elif(num2 == 7):
        num1 = 1
        num2 = 1
    elif(num3 == 7):
        num1 = 1
        num2 = 1
        num3 = -1
    
    product = num1 * num2 * num3
    
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(1,5,7)
print(product)
