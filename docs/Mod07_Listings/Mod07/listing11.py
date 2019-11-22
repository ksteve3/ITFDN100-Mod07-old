# ------------------------------------------------- #
# Title: Listing 11
# Description: A simple try-catch demo
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #
#47:00

# Using try
try:
 quotient = 5/0
 print(quotient)
except:
 print("There was an error! <<< Custom Message!\n")


# Now, without try
quotient = 5/0
print('never gets to this line')
