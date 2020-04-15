#DSA-Assgn-18

def find_unknown_words(text, vocabulary):
    words = text.split(" ")
    unknown_words = set()
    for word in words:
        if word not in vocabulary:
            unknown_words.add(word)
    
    if len(unknown_words) <= 0:
        return -1
        
    return unknown_words

#Pass different values of text and vocabulary to the function and test your program
text = "The sun rises in the east and sets in the west."
vocabulary = ["sun", "in", "rises", "the", "east"]
unknown_words = find_unknown_words(text, vocabulary)
print("The unknown words in the file are:", unknown_words)
