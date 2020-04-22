#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    if((month % 2 != 0 and month < 8) or (month % 2 == 0 and month > 7)):
        if(day == 31):
            next_day = 1
            if(month == 12):
                next_month = 1
                next_year = year + 1
            else:
                next_month = month + 1
                next_year = year
        else:
            next_day = day + 1
            next_month = month
            next_year = year
            
    elif(month != 2):
        if(day == 30):
            next_day = 1
            next_month = month + 1
            next_year = year
        else:
            next_day = day + 1
            next_month = month
            next_year = year
            
    elif(month == 2):
        if(day == 29):
            next_day = 1
            next_month = 3
            next_year = year
        elif(day == 28):
            if((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
                next_day = 29
                next_month = month
                next_year = year
            else:
                next_day = 1
                next_month = 3
                next_year = year
        else:
            next_day += 1
            next_month = 2
            next_year = year
    
    print(next_day,"-",next_month,"-",next_year)


generate_next_date(30, 6, 2015)
