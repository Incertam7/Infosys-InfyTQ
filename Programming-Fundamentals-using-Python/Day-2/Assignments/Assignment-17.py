#PF-Tryout

def find_new_salary(current_salary, job_level):
    # write your logic here
    hike = None
    
    if job_level == 3:
        hike = 0.15
    elif job_level == 4:
        hike = 0.07
    elif job_level == 5:
        hike = 0.05
    else:
        hike = 0
    
    new_salary = current_salary + (current_salary * hike)
    
    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary = find_new_salary(10000, 3)
print(new_salary)
