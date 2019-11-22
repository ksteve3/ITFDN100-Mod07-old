# ------------------------------------------------- #
# Title: Listing 6
# Description: Reading rows of data from a file with readlineS()
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
#20:34
# Data --------------------------------------------- #
strData = 'ID\nName'
strFileName = 'AppData.txt'
lstData = []

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


def read_file_data_to_list(file_name):
 """ Reads rows of data data from a file into a list
 :param file_name: (string) with name of file
 :return: (list) with rows of data read from the file
 """
 file = open(file_name, "r")
 data = file.readlines() # reads rows of data into a list object
 file.close()
 return data

# Presentation ------------------------------------- #
save_data(data=strData, file_name=strFileName)

print('Here is the first row of data from the file:')
lstData = read_file_data_to_list(file_name=strFileName)

print(lstData[0].strip()) # used strip() to remove newline
print(lstData[1].strip())

