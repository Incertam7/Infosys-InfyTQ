#DSA-Exer-15

def pattern_search(text, pattern):
    count = 0
    pattern_len = len(pattern)

    i = 0
    j = 0
    substring = ""
    
    for i in range(0, len(text) - pattern_len):
        if text[i : i + pattern_len] == pattern:
            count += 1

    return count

#Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result = pattern_search(text, pattern)
print("The given text:", text)
print("Pattern:", pattern)
print("No. of occurrences of the pattern :", result)
