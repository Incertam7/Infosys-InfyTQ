#PF-Assgn-19

def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0
    #write your logic here
    if(distance_in_kms <= 0 or quantity_ordered <= 0 or (food_type != 'V' and food_type != 'N')):
        bill_amount = -1
    else:
        if(food_type == 'V'):
            bill_amount = 120 * quantity_ordered
        elif(food_type == 'N'):
            bill_amount = 150 * quantity_ordered

        travel_cost = 0
        if(distance_in_kms < 3):
            travel_cost = 0
        elif(distance_in_kms >= 3 and distance_in_kms <= 6):
            travel_cost = (distance_in_kms - 3) * 3
        else:
            travel_cost = (3 * 3) + (distance_in_kms - 6) * 6
            
        bill_amount += travel_cost
        
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,3)
print(bill_amount)
