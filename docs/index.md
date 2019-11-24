# Title

 
 Dev: KStevens
 
 Date: 11.20.2019
 
 GitHub Markdown // Index.md Template 
 
  Reference: https://www.youtube.com/watch?v=4IkIdXJBC6o&feature=youtu.be, 1:23:24
  

## Structured Error Handling (Try-Except)
When you are programming, you fix your bugs immediately and make sure the code
runs smoothly. However, it often happens that other people introduce new bugs
when they use your program.

### Raising Custom Errors
Python automatically generates errors based on conditions defined by the
Python Runtime. However, you can also "raise" errors based on custom
conditions (Listing 13).

```
# ------------------------------------------------- #
# Title: Listing 13
# Description: A try-catch with manually raised errors
# ChangeLog: (Who, When, What)
# KStevens,11.20.2019,Created Script
# ------------------------------------------------- #
try:
 new_file_name = input("Enter the name of the file you want to make: ")
 if new_file_name.isnumeric():
 raise Exception('Do not use numbers for the file\'s name')
except Exception as e:
 print("There was a non-specific error!")
print("Built-In Python error info: ")
 print(e, e.__doc__, type(e), sep='\n')
```
#### Listing 13

![Github pages test image](https://ksteve3.github.io/ITFnd100-Mod07/Snips/test%20github%20image.PNG "Github pages test image")
#### Figure 13/ Github Test page. The Github Test page image.

![Remote images](https://i.ytimg.com/vi/l3oPTo4vCXI/maxresdefault.jpg "Remote images")
#### Remote images/ Github Test page. The Remote image.



```
# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Research Exception Handling & Pickling in Python
# ChangeLog (Who,When,What):
# Kstevens,11-20-19,Modified code to complete assignment 7
# ------------------------------------------------------------------------ #
# Research source: Python Tutorial: Using Try/Except Blocks for Error Handling,
# https://www.youtube.com/watch?v=NIWwJbo-9_8
# Research source (other/related to above): code_snippets/Exceptions/,
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Exceptions
# Research topic: Pickeling and scaling, https://pythonprogramming.net/pickling-scaling-machine-learning-tutorial/
# Code Version 7.?
#Pickling and Scaling, https://pythonprogramming.net/pickling-scaling-machine-learning-tutorial/

#import pickle
#with open('linearregression.pickle','wb') as f:
#    pickle.dump(clf, f)
#    pickle_in = open('linearregression.pickle','rb')
#clf = pickle.load(pickle_in)
#import Quandl, math
#import numpy as np
#import pandas as pd
#from sklearn import preprocessing, cross_validation, svm
#from sklearn.linear_model import LinearRegression
#import matplotlib.pyplot as plt
#from matplotlib import style
#import datetime
#import pickle
#
#style.use('ggplot')
#
#df = Quandl.get("WIKI/GOOGL")
#df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
#df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
#df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
#
#df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
#forecast_col = 'Adj. Close'
#df.fillna(value=-99999, inplace=True)
#forecast_out = int(math.ceil(0.1 * len(df)))
#
#df['label'] = df[forecast_col].shift(-forecast_out)
#
#X = np.array(df.drop(['label'], 1))
#X = preprocessing.scale(X)
#X_lately = X[-forecast_out:]
#X = X[:-forecast_out]
#
#df.dropna(inplace=True)
#
#y = np.array(df['label'])
#
#X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
#COMMENTED OUT:
#clf = svm.SVR(kernel='linear')
#clf.fit(X_train, y_train)
#confidence = clf.score(X_test, y_test)
#print(confidence)
#pickle_in = open('linearregression.pickle','rb')
#clf = pickle.load(pickle_in)
#
#
#forecast_set = clf.predict(X_lately)
#df['Forecast'] = np.nan
#
#last_date = df.iloc[-1].name
#last_unix = last_date.timestamp()
#one_day = 86400
#next_unix = last_unix + one_day
#
#for i in forecast_set:
#    next_date = datetime.datetime.fromtimestamp(next_unix)
#    next_unix += 86400
#    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]
#df['Adj. Close'].plot()
#df['Forecast'].plot()
#plt.legend(loc=4)
#plt.xlabel('Date')
#plt.ylabel('Price')
#plt.show()
```

