# Exception Handling & Pickling 

 Date: 11.21.19
 
 Descprition: File & Assignemnet documents for Module07
 
 Dev: Kstevens
 
 ITFDN100 A
 
 Assignment07

## Assignment07:
 (Overview)
 
 Research and document your knowledge about the use and benefits of the 
 Pickle module and exception handling in Python. The full assignment and further notes following 
 this week’s discussions can be viewed or downloaded here: [Assignment07.pdf](https://canvas.uw.edu/courses/1342958/files/59791641?module_item_id=9973247 "Assignment07.pdf") ,(external link),[_Mod7PythonProgrammingNotes.pdf](https://canvas.uw.edu/courses/1342958/files/59801217?module_item_id=9973246 "_Mod7PythonProgrammingNotes.pdf") ,(external link).


## Intro
The primary focus of week seven of Introduction to Python Programing, consisted of demonstrations on how to work with and configure error handling in Python which included the topics of try/except blocks, exception errors, built-in and custom error exceptions and exception classes, and Python’s Pickling Module. The secondary focus of this week was on learning how to use [basic writing and formatting syntax](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax "basic writing and formatting syntax") ,(external link) using Jekyll. used to build and present personal and professional scripting projects with GitHub Webpages. 
This week’s assignment consists of researching and documenting knowledge on the following bullet point topics and programming methods and presenting our research on GitHub Webpages using Jekyll’s writing and formatting syntax discussed in  Mod07 YouTube tutorial found at Module07 Course Video (external link), starting at 1:30:00.

The following topics will be briefly discussed in this document containing the sources and conclusions of my research pertaining to Assignment07’s research exercise detailed in Assigment07.pdf (external link).

•	Exception handling in Python 
•	Pickling in Python 

Exception handling in Python 
Search the web for examples of how to use Python’s exception handing features. Make note of the URL for any pages you feel are good at explaining the subject, and why you feel that way. 



### Raising Custom Errors
Python automatically generates errors based on conditions defined by the
Python Runtime. However, you can also "raise" errors based on custom
conditions (Listing 13).

```
# ------------------------------------------------- #
# Title: Listing 13
# Description: A try-catch with manually raised errors
# ChangeLog: (Who, When, What)
# KStevens,11.20.2019,Created Script
# ------------------------------------------------- #
try:
 new_file_name = input("Enter the name of the file you want to make: ")
 if new_file_name.isnumeric():
 raise Exception('Do not use numbers for the file\'s name')
except Exception as e:
 print("There was a non-specific error!")


print("Built-In Python error info: ")
 print(e, e.__doc__, type(e), sep='\n')
```
#### Listing 13
