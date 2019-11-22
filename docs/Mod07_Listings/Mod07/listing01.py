# ------------------------------------------------- #
# Title: Listing 1
# Description: Writing to a file with write()
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
#2:06
# Data --------------------------------------------- #
strData = 'test data'
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
# Presentation ------------------------------------- #
save_data(strData, strFileName)
print('Data Saved!')

