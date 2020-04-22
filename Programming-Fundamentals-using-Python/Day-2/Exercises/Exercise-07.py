#PF-Exer-7

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost = 0
    #Write your logic here
    rate_per_adult = 37550.0
    rate_per_child = 37550.0 / 3
    adultsTotal = no_of_adults * rate_per_adult
    childrenTotal = no_of_children * rate_per_child
    
    total_before_tax = adultsTotal + childrenTotal
    service_tax = 0.07 * total_before_tax
    
    gross_total = total_before_tax + service_tax
    total_ticket_cost = 0.9 * gross_total

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)
