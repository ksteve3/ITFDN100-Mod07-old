# ------------------------------------------------- #
# Title: Listing 8
# Description: Reading and Writing rows of file data
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
# Data --------------------------------------------- #
strFileName = 'AppData.txt'
# Processing --------------------------------------- #
def manage_file(file_name, mode, data = None):
 """ A custom wrapper function for the standard open() file function
 :param data: (string) with data to save
 :param file_name: (string) with name of file
 :param mode: (string) with name of mode [Write,Overwrite,Read]
 :return: (string) with data or write/append status
 """
 return_data = ''
 if mode.lower() == 'write':
  with open(file_name, "a") as file:
   file.write(data + "\n")
   return_data = 'New data added to file!'
 elif mode.lower() == 'overwrite':
  with open(file_name, "w") as file:
   file.write(data + "\n")
   return_data = 'File overwritten and new data added to file!'
 elif mode.lower() == 'read':
  for row in open(file_name, 'r'):
   return_data += row
 else:
   return_data = "No matching mode option"
 return return_data

# Presentation ------------------------------------- #
print("Type in a Customer Id and Name you want to add to the file")
print("(Enter 'Exit' to quit!)")
while(True):
 print('''
 Choose an option
 1 = Show Current Data
 2 = Add New Data
 3 = Create a New or an Overwrite File
 4 = Exit
 ''')
 choice = input('Enter an Option: ')
 if choice == '1':
  print('Here is the current data from the file:')
  print(manage_file(file_name=strFileName, mode='read').strip())
 elif choice == '2':
  new_data = input("Enter the ID and Name (ex. 1,Bob Smith): ")
  manage_file(file_name=strFileName, mode='write', data=new_data)
 elif choice == '3':
  manage_file(file_name=strFileName, mode='overwrite',
data='ID,Name')
 elif choice == "4":
  break
 else:
  print('Please Enter Choice 1,2,3, or 4!')
