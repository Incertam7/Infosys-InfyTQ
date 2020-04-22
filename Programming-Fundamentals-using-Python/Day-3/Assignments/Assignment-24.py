#PF-Assgn-24
def form_triangle(num1, num2, num3):
    #Do not change the messages provided below
    success = "Triangle can be formed"
    failure = "Triangle can't be formed"

    #Write your logic here
    if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
        return success
    else:
        return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1 = 7
num2 = 3
num3 = 5
print(form_triangle(num1, num2, num3))
