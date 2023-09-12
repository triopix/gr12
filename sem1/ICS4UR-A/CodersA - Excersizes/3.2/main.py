"""
Exercise 3.2 Can you identify and explain the errors in the following lines of code?
Correct them.

"""

"""
For this one, there is a period right after the parentheses - and this is not allowed

Fix: - Remove the parentheses/add the period inside the statement 

print("A message. ")
"""
# print("A message").


"""
Here the string is supposed to be enclosed by double quotes, but single quotes are used instead
Python thinks the single quote is part of the string. To fix this, keep the quotes synnonymous with whatever (singel or double)

Fix:

print("A message")

"""
# print("A message') 

# This case does not produce an error
# Here the best practice would either be to just use single quotes and not use double quotes
print('A messagef"' )