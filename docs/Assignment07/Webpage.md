# Assignment07:
	Dev: KStevens
	
	Date: 11.20.2019
	
	https://www.youtube.com/watch?v=4IkIdXJBC6o&feature=youtu.be, 1:23:24

## Exception Handling & Pickling
#### (Overview)

 Research and document your knowledge about the use and benefits of the 
 Pickle module and exception handling in Python. The full assignment and further notes following 
 this week’s discussions can be viewed or downloaded here: [Assignment07.pdf](https://canvas.uw.edu/courses/1342958/files/59791641?module_item_id=9973247 "Assignment07.pdf") ,(external link),[_Mod7PythonProgrammingNotes.pdf](https://canvas.uw.edu/courses/1342958/files/59801217?module_item_id=9973246 "_Mod7PythonProgrammingNotes.pdf") ,(external link).


## Structured Error Handling (Try-Except)
When you are programming, you fix your bugs immediately and make sure the code
runs smoothly. However, it often happens that other people introduce new bugs
when they use your program.

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
