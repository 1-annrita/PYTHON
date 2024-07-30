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
#     -can read data from a comma separated values (.csv) file into Python dictionaries for each row
# collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
# random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
# string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
# re: pattern-matching in strings via regular expressions
# math: some standard mathematical functions
# os: interacting with operating systems
#     -has a method for changing the current working directory
# os.path: submodule of os for manipulating path names
# sys: work directly with the Python interpreter
# json: good for reading and writing json files (good for web work)
# datetime: tell current time and date
# zipfile: can help extract all of the files from a zip file
# time: can say how long your code took to run





# TECHNIQUES FOR IMPORTING MODULES

# 1. To import an individual function or class from a module:
# from module_name import object_name
#2.  To import multiple individual objects from a module:
# from module_name import first_object, second_object
# 3. To rename a module:
# import module_name as new_name
# 4. To import an object from a module and rename it:
# from module_name import object_name as new_name
# 5. To import every object individually from a module (DO NOT DO THIS):
# from module_name import *
#     ```
#     6. If you really want to use all of the objects from a module, 
#       use the standard import module_name statement instead and access 
#       each of the objects with the dot notation.
#     ```python
# import module_name







# MODULES, PACKAGES AND NAMES

# In order to manage the code better, modules in the Python Standard 
# Library are split down into sub-modules that are contained within 
# a package. 
# A package is simply a module that contains sub-modules.
#  A sub-module is specified with the usual dot notation.

# Modules that are submodules are specified by the package name 
# and then the submodule name separated by a dot. 
# You can import the submodule like this.

# import package_name.submodule_name