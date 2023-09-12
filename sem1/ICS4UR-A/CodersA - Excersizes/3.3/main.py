"""
Exercise 3.3 When something is wrong with your code, Python will raise errors. Often
these will be “syntax errors” that signal that something is wrong with the form of your
code (e.g., the code in the previous exercise raised a SyntaxError). There are also “runtime
errors,” which signal that your code was in itself formally correct, but that something went
wrong during the code’s execution. A good example is the ZeroDivisionError, which in-
dicates that you tried to divide a number by zero (which, as you may know, is not allowed).
Try to make Python raise such a ZeroDivisionError.

"""

# zero division error as instructed by example

error = 0 / 0
print(error)