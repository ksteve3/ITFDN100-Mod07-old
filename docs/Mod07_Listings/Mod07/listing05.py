# ------------------------------------------------- #
# Title: Listing 5
# Description: Reading a number of rows from a file with readline()
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
#17:49
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


def read_some_data_rows(file_name, number_of_rows):
 """ Reads rows of string data from a file
 :param file_name: (string) with name of file
 :param number_of_rows: (int) with number of rows you want from the file
 :return: (list) with one or more data rows read from the file
 """
 counter = 0
 data = []
 file = open(file_name, "r")
 while counter < number_of_rows:
    data.append([file.readline()]) # APPENDING the data to a list
    counter += 1
 file.close()
 return data # returning the chosen row of data


def read_a_data_row(file_name, row_you_want):
 """ Reads rows of string data from a file
 :param file_name: (string) with the name of file
 :param row_you_want: (int) with the number of the row you want from the
file
 :return: (string) with one or more data rows read from the file
 """
 counter = 0
 file = open(file_name, "r")
 while counter < row_you_want:
    data = [file.readline()] # REPLACING the data in a list
    counter += 1
 file.close()
 return data # returning the chosen row of data


# Presentation ------------------------------------- #
save_data(data=strData, file_name=strFileName)

print('Here is the first row of data from the file:')
print(read_some_data_rows(file_name=strFileName, number_of_rows=1)) # new line character is not included!

print('Here is the first AND second row of data from the file:')
print(read_some_data_rows(file_name=strFileName, number_of_rows=2))

print('Here is the second row of data from the file:')
print(read_a_data_row(file_name=strFileName, row_you_want=2))
