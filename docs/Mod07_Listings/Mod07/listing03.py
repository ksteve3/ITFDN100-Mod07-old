# ------------------------------------------------- #
# Title: Listing 3
# Description: Adding data to a file with append()
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
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
def read_data(file_name):
 """ Reads all string data from a file
 :param file_name: (string) with name of file
 :return: (string) with data read from the file
 """
 file = open(file_name, "r")
 data = file.read() # read all the data in the file at once
 file.close()
 return data
def add_more_data(data, file_name):
 """ Saves string data to a file using APPEND Mode
 :param data: (string) with data to save
 :param file_name: (string) with name of file
 :return: nothing
 """
 file = open(file_name, "a")
 file.write(data + "\n")
 file.close()
# Presentation ------------------------------------- #
save_data(data=strData, file_name=strFileName)
print('Here is the beginning data from the file:')
print(read_data(file_name=strFileName))
add_more_data(data="even more test data", file_name=strFileName)
print('Here is the beginning AND the added data from the file:')
print(read_data(file_name=strFileName))
print('^ Note the extra blank line was read from the file too! ^')
