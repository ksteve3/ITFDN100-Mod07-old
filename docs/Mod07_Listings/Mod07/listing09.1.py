# ------------------------------------------------- #
# Title: Listing 9
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
#39:32 - https://www.google.com/search?q=pickle+python&oq=pickle+python&aqs=chrome..69i57j0l7.4396j0j7&sourceid=chrome&ie=UTF-8, https://www.google.com/search?sxsrf=ACYBGNR95cnBOyJPRRjcga8Komx1ux1-Gw%3A1574313917183&ei=vR_WXenqCozA0PEP1L258AU&q=working+with+pickles+and+bianary+files+python&oq=working+with+pickles+and+bianary+files+python&gs_l=psy-ab.3...21547.26771..27159...1.2..0.297.3074.1j0j12......0....1..gws-wiz.......0i71j35i304i39j0i333.GiVG55IIw-Y&ved=0ahUKEwipvbGuyPrlAhUMIDQIHdReDl4Q4dUDCAs&uact=5, https://www.google.com/search?q=working+with+bianary+files+python&oq=working+with+bianary+files+python&aqs=chrome..69i57j0l2.15961j0j7&sourceid=chrome&ie=UTF-8
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

print(objFileData.__str__())
