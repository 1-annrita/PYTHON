# Code A.
# def mean(num_list):
#     return sum(num_list) / len(num_list)

# def add_five(num_list):
#     return [n+5 for n in num_list]




# What if this script also includes executable statements in addition 
# to function definitions that we don't want to import
# Use  if__name__ =='__main__' ->We tell python to execute 
# this code only when the main program being executed is 
# this useful_functions.py




# Code B
def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()