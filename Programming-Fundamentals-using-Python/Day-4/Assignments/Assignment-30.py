#PF-Assgn-30

def encode(message):
    
    encoded_message = ""
    
    count = 1
    
    if len(message) == 1:
        encoded_message += "1" + message
    
    for i in range (0, len(message)):
        if i == len(message) - 1:
            if message[i] != message[i-1]:
                encoded_message += "1" + message[i]
        else:
            if(message[i] == message[i+1]):
                count += 1
            else:
                encoded_message += str(count) + message[i]
                count = 1
        
    return encoded_message
    
#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
