#PF-Assgn-31
def check_palindrome(word):
    
    flag = False
    
    for i in range(0, len(word)):
        if word[i] == word[-(i+1)]:
            flag = True
        else:
            flag = False
            break
    
    return flag
    
status = check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
