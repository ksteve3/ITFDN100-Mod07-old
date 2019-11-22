# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# <YourName>,<1.1.2030>,Created Script
# ------------------------------------------------- #
#41:20
import pickle # This imports code from another code file!
# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
 objFile = open(file_name, "ab")
 pickle.dump(list_of_data, objFile)
 objFile.close()

def read_data_from_file(file_name):
 file = open(file_name, "rb")
 list_of_data = pickle.load(file)
 file.close()
 return list_of_data

# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
intId = int(input("Enter an Id: "))
strName = str(input("Enter a Name: "))
lstCustomer = [intId, strName]

# TODO: store the list object into a binary file
save_data_to_file(strFileName, lstCustomer)

# TODO: Read the data from the file into a new list object and display the contents
print(read_data_from_file(strFileName)[0])
