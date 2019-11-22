# ------------------------------------------------- #
# Title: Listing 7
# Description: Reading rows of data from a file with a for loop
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
#23:00
# Data --------------------------------------------- #
strData = 'ID,Name\n1,Bob Smith'
strFileName = 'AppData.txt'
# Processing --------------------------------------- #

def save_data(data, file_name):
 """ Saves string data to a file
 :param data: (string) with data to save
 :param file_name: (string) with name of file
 :return: nothing
 """
 with open(file_name, "w") as file: # using the WITH option
  file.write(data + "\n")
 # file.close() # with automatically closes the file

def read_file_data_to_list(file_name):
 """ Reads rows of data data from a file into a list
 :param file_name: (string) with name of file
 :return: (list) of data rows read from the file
 """
 data = [] # you must initialize the list variable before you use it
 for row in open(file_name, 'r'):
  data.append(row) # read one row of data in the file per loop
 # automatically closes the file
 return data

# Presentation ------------------------------------- #
save_data(data=strData, file_name=strFileName)

print('Here are the first two rows of data from the file:')
print(read_file_data_to_list(file_name=strFileName)[0].strip())
print(read_file_data_to_list(file_name=strFileName)[1].strip())

