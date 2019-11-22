# ------------------------------------------------- #
# Title: Listing 13
# Description: A try-catch with multiple error messages
# https://docs.python.org/3/library/exceptions.html#bltin-exceptions
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
#55:24

try:
 quotient = 5/0
 f = open('SomeFile.txt', 'r+') # the read plus option gives an error if filed does not exist
 f.write(quotient) # causes an error if the file does not exist
 except Exception as e:
 print("There was a non-specific error!")
 print("Built-In Python error info: ")
 print(e, e.__doc__, type(e), sep='\n')
except ZeroDivisionError as e:
 print("Please do no use Zero for the second number!")
 print("Built-In Python error info: ")
 print(e, e.__doc__, type(e), sep='\n')
except FileNotFoundError as e:
 print("Text file must exist before running this script!")
 print("Built-In Python error info: ")
 print(e, e.__doc__, type(e), sep='\n')
