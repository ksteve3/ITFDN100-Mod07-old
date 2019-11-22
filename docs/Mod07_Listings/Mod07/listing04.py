# ------------------------------------------------- #
# Title: Listing 4
# Description: Reading a single line from a file with readline()
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
#9:20
# Data --------------------------------------------- #
strData = 'test data\nmore test data'
strFileName = 'AppData.txt'
# Processing --------------------------------------- #
def save_data(data, file_name):
 """ Saves string data to a file
 :param data: (string) with data to save
 :param file_name: (string) with name of file
 :return: nothing
 """
 file = open(file_name, "w")
 file.write(data + "\n")
 file.close()

def read_data_row(file_name):
 """ Reads a row of string data from a file
 :param file_name: (string) with name of file
 :return: (string) with one row of data from the file
 """
 file = open(file_name, "r")
 # readline() acts like a "cursor"
 data = file.readline() # read one row of data in the file
 file.close()
 return data

# Presentation ------------------------------------- #
save_data(data=strData, file_name=strFileName)


print('Here is the first row of data from the file:')
print(read_data_row(file_name=strFileName))
print('^ Note the extra blank line was read from the file too! ^')


print('Here is the SAME row of data from the file:')
print(read_data_row(file_name=strFileName))

