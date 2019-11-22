# ------------------------------------------------- #
# Title: Listing 12
# Description: A try-catch with better error messages
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
#50:00

try:
 quotient = 5/0
 print(quotient)
except Exception as e:
 print("There was an error! << Custom Message")

 print("Built-In Pythons error info: ")
 print(e)
 print(type(e))
 print(e.__doc__)
 print(e.__str__())
