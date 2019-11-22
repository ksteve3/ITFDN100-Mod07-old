# ------------------------------------------------- #
# Title: Listing 9
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
#33:00 - https://www.google.com/search?q=pickle+python&oq=pickle+python&aqs=chrome..69i57j0l7.4396j0j7&sourceid=chrome&ie=UTF-8
import pickle # This imports code from another code file!

intId = int(input("Enter an Id: "))
strName = str(input("Enter a Name: "))
lstCustomer = [intId, strName]
print(lstCustomer)

# Now we store the data with the pickle.dump method
objFile = open("AppData.dat", "ab")
pickle.dump(lstCustomer, objFile)
objFile.close()

# And, we read the data back with the pickle.load method
objFile = open("AppData.dat", "rb")
objFileData = pickle.load(objFile) #load() only loads one row of data.
objFile.close()

print(objFileData)
