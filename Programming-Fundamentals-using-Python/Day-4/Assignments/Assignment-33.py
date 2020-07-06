#PF-Assgn-33

def find_common_characters(msg1,msg2):
    
    common_characters = ""
    
    if len(msg1) <= len(msg2):
        for char in msg1:
            if char in msg2 and char not in common_characters:
                common_characters += str(char)
    
    if len(common_characters) == 0:
        return -1
    
    return common_characters

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
