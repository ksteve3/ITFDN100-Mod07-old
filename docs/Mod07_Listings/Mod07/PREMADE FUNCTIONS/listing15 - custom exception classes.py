# ------------------------------------------------- #
# Title: Listing 15
# Description: A try-catch with manually raised errors
# using custom error classes
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
#1:08:30
class CustomError(Exception):
 """ Some custom error info in the DocString """
 def __str__(self):
  return 'Some custom error message'
class FileNotTXTError(Exception):
 """ File extension must end with txt to indicate it is a text file """
 def __str__(self):
  return 'File extension not txt'


try:
 new_file_name = input("Enter the name of the file you want to make: ")
 if new_file_name.isnumeric():
  raise Exception('Do not use numbers for the file\'s name')
 elif new_file_name.endswith('txt') == False:
  raise FileNotTXTError()
 else:
  raise CustomError()

except FileNotTXTError as e:
 print("There was a non-specific error!")
 print("Built-In Python error info: ")
 print(e, e.__doc__, type(e), sep='\n')

except Exception as e:
 print("There was a non-specific error!")
 print("Built-In Python error info: ")
 print(e, e.__doc__, type(e), sep='\n')


# TODO: add more except sections to capture the specific derived exceptions!

