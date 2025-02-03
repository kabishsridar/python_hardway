#now introducing def funct.
#now the word breaks up
def break_words(stuff):    
    """THis functionwill break up words for us."""
    words  = stuff.split(' ')
    return words
#now sorting in alphabetic order
def sort_words(words):    
    """sorts the words . """
    return sorted(words)
#now printing only first word
def print_first_word(words):    
    """prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
#now printing only last word
def print_last_word(words):    
    """prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)
#now sorting sentence
def sort_sentence(sentence):    
    """Takes in a full sentence and returns the sorted words . """
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(setence):    
    """prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):    
    """sorts the wods then prints the first and last one . """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

sentence = "All good things come to those who wait." 
print_first_and_last_sorted(sentence)
print(sort_sentence(sentence))
print(break_words(sentence))