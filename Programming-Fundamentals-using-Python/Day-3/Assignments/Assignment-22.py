#PF-Assgn-22
def find_leap_years(given_year):

    list_of_leap_years = []
    temp = given_year
    
    # Write your logic here
    if check_leap_year(given_year):
        temp = given_year
    elif check_leap_year(given_year + 1):
        temp = given_year + 1
    elif check_leap_year(given_year + 2):
        temp = given_year + 2
    elif check_leap_year(given_year + 3):
        temp = given_year + 3
    
    for i in range(1, 16):
        if(temp == given_year):
            list_of_leap_years.append (temp + i * 4)
        else:
            list_of_leap_years.append (temp + (i - 1) * 4)


    return list_of_leap_years

def check_leap_year(given_year):
    if given_year % 400 == 0:
        return True
    elif given_year % 4 == 0 and given_year % 100 != 0:
        return True
    else:
        return False

list_of_leap_years = find_leap_years(2002)
print(list_of_leap_years)
