# A function called count_words that takes a string as an argument 
# and returns the number of words in that string.

def count_words(string):
    if string == "":
        return ""
    else:
        return len(string.split())