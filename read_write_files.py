# READING FILES

# CODE A
# f = open('C:/Users/RITA/ritapython/some_file.txt' , 'r')
# file_data = f.read()
# f.close()
# print(file_data)


#CODE B
# f = open('C:/Users/RITA/Downloads/PYTHON-SCRIPTING.txt' , 'r')
# file_data = f.read()
# f.close()
# print(file_data)



# WRITING TO FILES


# CODE C
# f = open('C:/Users/RITA/ritapython/some_file.txt' , 'w')
# file_data = f.write("My name is AnnRita Mukami. \nI go to Safaricom Academy.\nI am 12 years old.")
# f.close()
# print(file_data)



#TOO MANY OPEN FILES


# CODE D
# files = []
# for i in range(10000):
#     files.append(open('some_file.txt', 'r'))
#     print(i)




# WITH


# A special syntax that auto-closes a file once you are 
# finished using it.
# With keyword allows you to open a file, do operations on it, 
# and automatically close it after the indented code is executed
# You can only access the file object,f,
# within this indented block

# CODE E
# with open('some_file.txt' , 'r') as f:
#     file_data = f.read()
#     print(file_data)




# CALLING THE READ METHOD WITH AN INTEGER

# Each time we called read on the file with an integer argument,
# it read up to that number of characters, outputted them, 
# and kept the 'window' at that position for the next call 
# to read

# CODE F
# with open("some_file.txt") as song:
#     print(song.read(4))
#     print(song.read())




# READING LINE BY LINE

# A
# \ns in blocks of text are newline characters. 
# The newline character marks the end of a line, 
# and tells a program (such as a text editor) to 
# go down to the next line. However, looking at the stream
# of characters in the file, \n is just another character.
# Fortunately, Python knows that these are special characters
# and you can ask it to read one line at a time.

with open('C:/Users/RITA/ritapython/some_file.txt') as f:
    line1 = f.readline()
    print(line1)
    line2 = f.readline()
    print(line2)





# B
# Conveniently, Python will loop over the lines of a file 
# using the syntax for line in file. I can use this to 
# create a list of lines in the file. Because each line 
# still has its newline character attached, I remove 
# this using .strip().


# CODE G
# camelot_lines = []
# with open("some_file.txt") as f:
#     for line in f:
#         camelot_lines.append(line.strip())

# print(camelot_lines)








# QUIZ:FLYING CIRCUS CAST LIST
# You're going to create a list of the actors who appeared 
# in the television programme Monty Python's Flying Circus.

# Write a function called create_cast_list that takes a 
# filename as input and returns a list of actors' names.
# It will be run on the file flying_circus_cast.txt
#  (this information was collected from imdb.com). 
# Each line of that file consists of an actor's name, 
# a comma, and then some (messy) information about roles 
# they played in the programme. You'll need to extract only 
# the name and add it to a list. You might use the .split()

def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for name in f:
            cast_list.append(name.split(",")[0])
            
    return cast_list
cast_list = create_cast_list('flying_circus_cast.txt')
print(cast_list)