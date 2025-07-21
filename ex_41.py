import random # importing modules
import sys
from urllib.request import urlopen # import urllib to download a list of words
from datetime import datetime

# URL containing words
word_url = "http://learncodethehardway.org/words.txt"
words = []
fileout = open('python_hardway\\ooplog_data.txt', 'a') # opening a file in write mode to store the questions, inputs, and answers
# Dictionary of code snippets and their English descriptions
phrases = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "Class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "Class %%% has-a function *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with self and parameters @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# Determine whether to show English phrases first
phrase_first = len(sys.argv) == 2 and sys.argv[1] == "english"

# Load words from the URL
for word in urlopen(word_url).readlines():
    words.append(str(word.strip(), encoding="utf-8"))
# print(words)

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(words, snippet.count("%%%"))]
    other_names = random.sample(words, snippet.count("***"))
    param_names = []
    results = []

    for _ in range(snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(words, param_count)))

    for sentence in (snippet, phrase):
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%", word, 1) # in place of %%% the words from the url will be replaced
        for word in other_names:
            result = result.replace("***", word, 1)
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

try:
    while True:
        snippets = list(phrases.keys())
        random.shuffle(snippets)
        print(snippets)

        time = datetime.now()
        fileout.write(str(time) + "\n")

        for snippet in snippets:
            phrase = phrases[snippet]
            question, answer = convert(snippet, phrase)
            # print(question, answer)
            if phrase_first:
                question, answer = answer, question

            fileout.write("QUESTION:") # to write the questions into the file
            fileout.write("\n")
            print(question) # displays the question in terminal
            fileout.write(f"{question} \n")
            usr_input = input(">")
            fileout.write(f"USER INPUT: {usr_input} \n")
            answer = (f"ACTUAL ANSWER: {answer}\n\n")
            print(answer)
            fileout.write(answer)
        fileout.close() # closing the file at last

except EOFError:
    print("\nBye")