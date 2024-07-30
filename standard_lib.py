# The Standard Library
# Explore the Python Standard Library for Python version 3.6 here:
# (opens in a new tab)https://docs.python.org/3.6/library/index.html(opens in a new tab). (Note for other versions of Python you can substitute a different version in the URL.)

# You can also discover new modules at the Python Module of the Week
# (opens in a new tab) blog.



# Code A.
# import math
# print(math.factorial(5))





# Code B.

# Import the `random` module
import random

# We begin with an empty `word_list`
word_file ='words.txt'
word_list =[]

# We fill up the word_list from the `words.txt` file
with open(word_file, 'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        if 3 < len(word)<8:
            word_list.append(word)

# Add your function generate_password below
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)


password = generate_password()
print(password)

# csv: very convenient for reading and writing csv files
# collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
# random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
# string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
# re: pattern-matching in strings via regular expressions
# math: some standard mathematical functions
# os: interacting with operating systems
# os.path: submodule of os for manipulating path names
# sys: work directly with the Python interpreter
# json: good for reading and writing json files (good for web work)