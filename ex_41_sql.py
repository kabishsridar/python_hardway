import random
import sys
from urllib.request import urlopen # import urllib to download a list of words
import mysql.connector as sqltor

mycon = sqltor.connect(host='localhost', user='root', passwd='2007kabish', database='python')
if mycon.is_connected():
    print("connected to database, the inputs will be stored to mysql")
else:
    print("Failed connecting to database")
cur = mycon.cursor()

# URL containing words
word_url = "http://learncodethehardway.org/words.txt"
words = []

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
            result = result.replace("%%%", word, 1)
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

        for snippet in snippets:
            phrase = phrases[snippet]
            question, answer = convert(snippet, phrase)
            # print(question, answer)
            if phrase_first:
                question, answer = answer, question

            print(question)
            usr_input = input(">")
            print(f"ANSWER: {answer}\n\n")
            command = "INSERT INTO OOPLOG_DATA (questions, user_answer, actual_answer) VALUES (%s, %s, %s)"
            values = (question, usr_input, answer)
            cur.execute(command, values)
            mycon.commit()

except EOFError:
    print("\nBye")