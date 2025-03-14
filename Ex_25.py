sentence = "All good things come to those who wait." 
word ="Kailash"

def break_words(stuff):    
    """This function will break up the words for us."""
    words = stuff.split(" ")
    return words  # Return the list of words

# Now sorting in alphabetic order
def sort_words(words):    
    """Sorts the words."""
    return sorted(words)

# Now printing only the first word
def print_first_word(words):    
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

# Now printing only the last word
def print_last_word(words):    
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

# Now sorting the sentence
def sort_sentence(sentence):    
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):    
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):    
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# Testing the functions
words = break_words(sentence)
print(words)
print_first_word(words[:]) 
print_last_word(words[:]) 
print(sort_sentence(sentence))
print(sort_words(break_words(word)))
print_first_and_last_sorted(sentence)
print_first_and_last(sentence)
