# ------------------------------------------------- #
# Title: Listing 14
# Description: A try-catch with manually raised errors
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
try:
 new_file_name = input("Enter the name of the file you want to make: ")
 if new_file_name.isnumeric():
  raise Exception('Do not use numbers for the file\'s name')
except Exception as e:
 print("There was a non-specific error!")
 print("Built-In Python error info: ")
 print(e, e.__doc__, type(e), sep='\n')
