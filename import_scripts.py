# IMPORT PYTHON CODE FROM OTHER SCRIPTS
# WORKING WITH import_scripts.py & demo.py

# If the Python script you want to import is in the same directory 
# as your current script, type import followed by the name of the 
# file without the dot py extension

# Code A.
# import demo
# print(4)


# To access objects in import_scripts.py, we need to use the name of
# the file followed by a dot followed by the object to tell Python to
# look for this object in the import_scripts file we imported

# Code B.
import demo
print(demo.num)


# When Python runs the script, it only has direct access to objects 
# defined in the script
# One of these objects is a module called demo
# A MODULE is just a file with Python definitions and statements

