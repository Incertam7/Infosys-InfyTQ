#PF-Tryout
def find_armstrong(number):
    sum = 0
    temp = number
    while(number != 0):
        remainder = number % 10
        number = number // 10
        sum += (remainder*remainder*remainder)
    if(sum == temp):
        return True
    return False

number = 370
if(find_armstrong(number)):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
