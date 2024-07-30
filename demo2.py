# Code A.
# import useful_functions

# scores = [88,92,79,93,85]

# mean = useful_functions.mean(scores)
# curved = useful_functions.add_five(scores)

# mean_c = useful_functions.mean(curved)

# print("Scores:", scores)
# print("Original Mean;", mean, " New mean:", mean_c)






# Make it simpler by adding an alias for useful_functions as uf
# Useful when we have objects we want to import from other python 
# scripts like functions





# Code B.
# import useful_functions as uf

# scores = [88,92,79,93,85]

# mean = uf.mean(scores)
# curved = uf.add_five(scores)

# mean_c = uf.mean(curved)

# print("Scores:", scores)
# print("Original Mean;", mean, " New mean:", mean_c)






#Code C.
import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)