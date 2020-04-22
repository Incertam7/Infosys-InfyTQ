#PF-Exer-22

def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    #Write your logic here
    ticket_number = airline + ":" + source[0:3] + ":" + destination [0:3]
    
    if no_of_passengers < 5:
        start_ticket = 101
        for i in range(0, no_of_passengers):
            ticket_number_list.append(ticket_number + ":" + str(start_ticket))
            start_ticket += 1
    
    else:
        start_ticket = 101 + (no_of_passengers - 5)
        for i in range(0, 5):
            ticket_number_list.append(ticket_number + ":" + str(start_ticket))
            start_ticket += 1
    
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI", "Bangalore", "London", 3))
