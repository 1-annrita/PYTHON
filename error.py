# x = int(input("Enter a number: "))
# print(x)

# print("Hello world!")



# The code inside the try block is first run
# If Python runs into any exceptions while 
# it's running that block
# it will jump to the code in the except block



# try:
#     x = int(input("Enter a number: "))
# except:
#     print('That\'s not a valid number')

# print('\nAttempted Input')




# If we want this code to keep running until
# the user inputs a valid number,
# we can use a while loop and break the loop 
# if all the code in the try block successfully executes


# while True:
#     try:
#         x = int(input("Enter a number: "))
#         break
#     except:
#         print('That\'s not a valid number')
#     finally:
#         print('\nAttempted Input')




# Exit program with ctrl+c, doesn't stop the program
# Because except handles any error, 
# including KeyboardInterrupt error
# Use ValueError exception 

# while True:
#     try:
#         x = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print('That\'s not a valid number')
#     finally:
#         print('\nAttempted Input')


# Handler address more than one type of exception
# 1.include a tuple afer except
# 2.Or if we want to execute different blocks of code
# depending on the exception, use multiple except blocks

while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print('That\'s not a valid number')
    except KeyboardInterrupt:
        print('\nNo input taken')
    finally:
        print('\nAttempted Input')






# ZeroDivisionError - raised when a program attempts to perform
# a division operation where the denominator is zero

# PARTY PLANNER

# def party_planner(cookies,people):
#     leftovers = None
#     num_each = None

#     try:
#         num_each = cookies // people
#         leftovers = cookies % people
#     except ZeroDivisionError:
#         print("Oops, you entered 0 people will be attending.")
#         print("Please enter a good number of people for a party")

#     return(num_each,leftovers)
# print(party_planner(40,5))