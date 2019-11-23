# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Research Exception Handling & Pickling in Python
# ChangeLog (Who,When,What):
# Kstevens,11-20-19,Modified code to complete assignment 7
# ------------------------------------------------------------------------ #
#Research source: Python Pickle Module for saving objects (serialization), https://www.youtube.com/watch?list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&time_continue=52&v=2Tw39kZIbhs&feature=emb_logo
    #Research source (other/related to above): 11.1. pickle — Python object serialization, https://docs.python.org/2/library/pickle.html
#Research topic: Pickle Module
#Code Version 7.4
#Example description: *Successful code (assuming "test_file.txt" exists in corresponding directory)


import pickle

example_dict = {1:"6",2:"2",3:"f"}

pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)

print(example_dict)
print(example_dict[2])
