#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    # write your logic here
    p_count = 0
    o_count = 0
    e_count = 0
    
    for i in range(1, len(patient_medical_speciality_list)):
        if patient_medical_speciality_list[i] == 'P':
            p_count += 1
        elif patient_medical_speciality_list[i] == 'O':
            o_count += 1
        elif patient_medical_speciality_list[i] == 'E':
            e_count += 1
        i += 1
    
    maxPatients = max(p_count, o_count, e_count)
    
    speciality = ""
    
    if(maxPatients == p_count):
        speciality = "P"
    elif(maxPatients == o_count):
        speciality = "O"
    else:
        speciality = "E"
    
    return speciality

def max(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        return num1
    elif(num2 > num3):
        return num2
    else:
        return num3

#provide different values in the list and test your program
patient_medical_speciality_list = [301, 'O', 302, 'O', 305, 'E', 401, 'E', 656, 'E']
medical_speciality = {"P":"Pediatrics", "O":"Orthopedics", "E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list, medical_speciality)
print(speciality)
