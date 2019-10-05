#!/usr/bin/env python
# coding: utf-8

# # Python Introduction
# 2018/10/18
# [tgp27@cam.ac.uk](mailto:tgp27@cam.ac.uk)
# 
# ## Sources
# Content based on 
# * [Python Standard Library](https://docs.python.org/3/library/) 
# * [NumPy manual](https://docs.scipy.org/doc/numpy/)
# * [Pandas manual](http://pandas.pydata.org/pandas-docs/stable/)
# * [Wikibook on Intro to Python](https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial)
# * [Hands On intro to Python](https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/index.html)
# 
# 
# ## Contents
# ### General features
# * Assigning values
# * Output: printing
# * Input
# * Comments
# 
# ### Data types
# * Integers and floats
# * Strings
# * Lists, Tuples and Sets
# * Dictionaries
# * Booleans and Comparison Operators
# * NumPy arrays
# * Pandas dataframes
# 
# ### Simple maths
# * Comparisons and Boolean operations
# * Arithmetic
# 
# ### Conditionals
# * if, elif, else Statements
# 
# ### Loops
# * for Loops
# * while Loops
# * break and continue statements
# * try and except statements
# 
# ### Functions
# * general functions
# * lambda expression
# * list functions, map and filter
# 
# ### Other Python objects
# * Classes
# * Modules and Packages
# 
# ____

# ## General features

# ### Assigning values to variables
# A variable (object) can be assigned a value using the '=' symbol:

# In[124]:


x = 4
y = 'hello there'


# The assigned value can be removed using the *del* keyword

# In[68]:


x = 3
del x
x


# ### Printing (code output)
# 
# You can force the code to print (i.e. give out) any object or value. Printing is a useful way for you to follow what the code is doing

# In[1]:


x = 3
y = 4
z = x + y
print(z)


# ### Input 
# If you're writing code in Jupyter or some other text editors, you can ask the user for text input

# In[1]:


player = input("Prof. Oak: Now, what did you say your name was? ")
print(player,", are you ready? Your very own Pokémon story is about to unfold.")


# [More info on input and output in Python](https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html)

# ### Comments
# Comments are sections of a code file that aren't a functional part of what the code does (see example below). They are created by adding the symbol \# (known by various names, such as hash or pound sign) to the front of a line of text.
# 
# 'Comments' can be helpful notes to the reader about what the code is doing. They can also be used to "switch off" sections of code, making them inoperative but not deleting the text, so you can "switch it on" again later.

# In[8]:


# Here are some numbers
print('One')
# print('Two')
# print('Three ')


# ## Data types

# ### Trivial data types
# * None: a variable can have type None (no value, not even zero)
# * Boolean logic: True and False are a separate data type used for logical statements (more on this later)

# ### Numeric types: integers and floats
# 
# Numbers in Python can be one of [three types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex): integers (2 and -3), floats (like 2.1 and 0.0) or complex numbers (like 1 + j).

# In[15]:


# Turn integers into floats
x = float(3)
print(x)


# In[11]:


#  Turn floats into integers. Rounding.
x = int(2.0)
y = int(-0.3)

print(x,y) #print x, then y


# ### Strings
# Textual data in Python is handled with objects called [strings](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).
# 
#  

# In[69]:


print('Hey there')


# A string containing an apostrophe can be written using "double quotes"

# In[70]:


print("It's fine. No really, it's fine.")


# Strings covering more than one line of code can be written using triple quote, either '''single''' or """double"""

# In[29]:


x = """Nature and Nature's laws lay hid in night;
God said, 'Let Newton be!' and all was light. 
(Alexander Pope, 1727)"""
print(x)


# Strings can be joined together using maths-style addition

# In[36]:


x = 'easy'
y = ' '
z = 'tiger'
print(x + y + z)


# Strings can be split using the .split() function, at the spaces or any other given point

# In[151]:


x = 'raise the roof'
a = x.split()
print(a)

# divide the string by removing the given sub-string
b = x.split(' the ')
print(b)


# Also note that the comment symbol \# doesn't turn the line into a comment if it's inside a string

# In[18]:


print('Number #0')


# ### Sequence types : lists, tuples and range
# [More on sequence types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
# 
# #### Indexing - selecting items from sequences
# 
# In an ordered sequence of objects, a given object is selected by specifying its index. For example, a string behaves as an ordered sequence of letters. Remember that counting in Python starts from zero. 

# In[43]:


str1 = 'hey there'
char1 = str1[0]
char2 = str1[2]
print(char1, char2)


# #### Lists
# Lists [  ] are ordered sequences of mixed objects (known as the *elements* of the string). The elements can be strings, numbers, lists or other data types
# 
# The length of a list (or other sequence object) can be checked using the len() function.

# In[70]:


list1 = ['a', 'b', 'c']
list2 = [1,2,3]
list3 = ['do','re', 3, list1, list2]
print(list3[4])
print(len(list3))


# In lists, new values can be assigned to list elements:

# In[51]:


list4 = [1,2,4,8,16]
list4[3] = 5
print(list4)


# We can also append new values to the list. Note that this can't be used to join together two lists - but that's easily done with a + symbol.

# In[143]:


list5 = [] # initially empty
list5.append(6)
print(list5)

list5.append([7,8,9])
print(list5)

list6 = [1,3,6]
list7 = [7,10,13]
print(list6+list7)


# #### Tuples
# 
# Tuples (  ) are a lot like lists, except they are not editable (therefore good for assigning values that you don't want the user to be able to change later). It's also Python convention to use tuples for homogeneous sequences (e.g. all numbers) and lists for heterogeneous (mixed) sequences.

# In[53]:


list5 = [1,2,3]
list5[0] = -3
print(list5)

tup1 = (1,2,3)
# next line gives error
tup1[0] = -3


# #### Ranges
# Ranges are sequences of numbers in a given range, useful for loops (see later)

# In[57]:


# range of 10
list6 = list(range(10))
print(list6)

# from 5 to 11 (note it stops at 10!)
list7 = list(range(5, 11))
print(list7)

# 0 to 30 in steps of 5
list8 = list(range(0, 30, 5))
print(list8)


# ### Dictionaries - the mappable data type

# In Python, a dictionary is a special kind of list with keys assigned to values (the key is the 'word' and the value is the 'definition' in the analogy to a dictionary).
# 
# Keys can be integers or strings. Values can be pretty much anything.
# 
# Dictionaries can be formed in many possible ways from a given paired set of keys and values

# In[80]:


a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e
print(b.keys())
print(c.values())


# New values can be assigned in a manner similar to lists. 
# 
# Keys and values can be deleted using the del keyword.
# 
# New pairs can be appended using the .update() function.

# In[76]:


a = dict(red=1, green=2, blue=3)
a['red'] = 0
del a['blue']
a.update({'yellow':5})
print(a)


# ### NumPy arrays
# A discussion of numpy arrays is not part of a typical introduction to Python, but is likely you will be using numpy arrays extensively. 
# 
# [More info from the SciPy manual](https://docs.scipy.org/doc/numpy-1.15.1/reference/arrays.html)
# 
# The following is taken from the NumPy website:
# 
# An array is a multidimensional container of items of the same type and size. The number of dimensions and items in an array is defined by its shape, which is a tuple of N positive integers that specify the sizes of each dimension. The type of items in the array is specified by a separate data-type object (dtype), one of which is associated with each ndarray.
# 
# As with other container objects in Python, the contents of an array can be accessed and modified by indexing or slicing the array (using, for example, N integers), and via the methods and attributes of the array.
# 
# An array can be created by lists of rows nested into a list of columns (see below). Once an array is defined, the shape and data type (dtype) of an array can easily be extracted:

# In[87]:


import numpy as np
array1 = np.array([[1, 2, 3], [4, 5, 6]])
print(array1.shape)
print(array1.dtype)


# Array indexing works like a regular matrix (row then column, counting from 0)

# In[92]:


#import numpy as np
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(array2[0,0])
print(array2[1,2])


# We can obtain a slice through the data using ':' instead of a specific index:

# In[93]:


#import numpy as np
array3 = np.array([[1, 2, 3], [4, 5, 6]])
print(array3[:,0])
print(array3[1,:])


# Some useful special arrays from numpy:
# * np.zeros((row, col)) for all zeros
# * np.empty((row, col)) for an empty array (default is also zeros)
# * np.identity(N), NxN square identity matrix
# * np.full((row, col), value), array full of a given value

# In[100]:


#import numpy as np
array4 = np.zeros((1,4))
print(array4)

array5 = np.empty((2,3))
print(array5)

array6 = np.identity(2)
print(array6)

array7 = np.full((1,7),'ha')
print(array7)


# ### Pandas dataframes
# 
# For large tables of data, it is convenient to use the pandas package, which introduces the [DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) type.
# 
# A dataframe is a little like a dictionary or a numpy array. Each column of data has a text heading, with the row written as a 1D array.

# In[105]:


import pandas as pd
dat = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=dat)
df


# A dataframe can also be created from a numpy array directly.

# In[107]:


#import pandas as pd
arr = [[1,2,3],[4,5,6],[7,8,9]]
df2 = pd.DataFrame(arr, columns=['one','two','three'])
df2


# Conversely, a dataframe can be converted into a numpy array (making it easy to use pandas and numpy together).

# In[115]:


#import pandas as pd
arr = [[1,2,3],[4,5,6],[7,8,9]]
df3 = pd.DataFrame(arr, columns=['one','two','three'])
new_arr = df3.values
print(new_arr)


# Selecting a column or row from the dataframe is similar to dictionary. [More info](https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/#iloc-selection)

# In[122]:


#import pandas as pd
arr = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
df4 = pd.DataFrame(arr, columns=['one','two','three'])
# get column
print(df4['three'])
# get some rows
df4.iloc[0:3]


# A complete list of functions for dataframes can be found in the [pandas manual](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)

# ### Other data types
# There are lots of other data types we haven't mentioned, such as [mathematical sets](https://docs.python.org/3/c-api/set.html), which are covered in online manuals and tutorials.

# ## Mathematical operations

# ### Logical Comparisons
# Statements in Python can be verified using the standard mathematical relations
# * '==' for equals
# * '!=' for not equal
# * '<' and '<=' for less than and less than or equal to
# * '>' and '>=' for less than and less than or equal to
# * 'is' and 'is not' can also be written to check equality
# * 'in' and 'not in' can be used to check if an element is in a list or sequence object

# In[125]:


x = 1
y = 1
z = [2,3]
print(x==1)
print(y!=1)
print(x>y)
print(x>=y)
print(x is not y)
print(x in z)


# ### Boolean logic
# We can use 'and', 'not' and 'or' to combine together comparisons.

# In[146]:


x = 1
y = 1
print(x<y or x==y)
print(not x==y) #not True = False
print(x==y and x!=y)


# ### Arithmetic
# The standard maths operations mostly use their usual symbols (but note the expections)
# * addition + and substraction -
# * multiplication \* and division \/
# * exponentials (powers) \*\*
# * modulo \%
# * floor division //

# In[132]:


print(1+2)
print(3-2)
print(8*9)
print(9/7)
print(7**3)
print(13%3)
print(9//4) # = 2.25


# ## Conditionals
# 
# Sometimes it is useful to write pieces of codes that are only activated under specific conditions. 
# 
# This can be achieved using conditionals, also called 'if statements'. A conditional is introduced using a keyword followed by a logical statement. The conditional ends with a colon (:). 
# 
# When the condition is met, the indented piece of code below the condition statement will run. This section of code will not run otherwise, and after Python reaches the end it will continue with the rest of the script.
# 
# The three big keywords here are *if*, *else* and *elif* (a combination and if and else). It's easy to see what these words do with an example (see below).

# In[157]:


x = 0
y = 1

if x < y:
    print("It's smaller")
elif x == y:
    print("They're equal")
else:
    print("It's larger")
    
print('Finished!')


# Some more examples:

# In[161]:


if True:
    print('hey')
if False:
    print('bye')


# Conditionals can also be nested

# In[176]:


x = 17
if x > 10:
    if x > 20:
        print('Extra large')
    else:
        print('Large')
else:
    print('Small')


# ## Loops
# It is sometimes useful to be able to run a section of code many times (rather than copying out the code over and over), which can be achieved using for loops. 
# 
# * For loops run a section of code for each value in a sequence (usualy lists or ranges).
# * While loops run a section of code so long as a given condition is satisfied.
# 
# Like conditionals, for loops can be nested.
# 
# ### For loops

# In[167]:


rg = range(-1,5)
for num in rg:
    z = num**2
    print(z)


# In[169]:


list1 = ['Tom','Dick','Harry']

for item in list1:
    print('Hey ' + item)


# If we want to calculate cumulative values, there is a shorthand (+= or -=).

# In[172]:


rg = range(1,8)

final_sum1 = 0
final_sum2 = 0
neg_sum = 0
for num in rg:
    final_sum1 = final_sum1 + num
    final_sum2 += num
    neg_sum -= num
print(final_sum1)
print(final_sum2)
print(neg_sum)


# ### While Loops

# In[183]:


temp = 18
while temp < 21:
    print("Temperature is", temp, "Celsius. It's too cold.")
    temp = temp+1
print("It's warm enough now")


# ### Break and continue statements 
# 
# If you want the code to stop once a condition has been satisfied, you can use the break keyword

# In[186]:


rg = range(1,10)
for n in rg:
    print(n)
    if n == 5:
        print('Reached five. Terminating now.')
        break


# The continue statement can be used to return to the loop once a sub-section of code has been run

# In[190]:


# continue returns us straight to the top
for letter in 'hey there':
    if letter == 'h':
        continue
    print(letter)


# ### Exceptions - try and except
# During loops (and elsewhere in Python programming) there may be circumstances when the code will produce an error for a given input. By default Python will stop interpeting the code at the line where the error occurs and will not continue reading the rest of the code. We can tell Python to over-ride this.
# 
# If something has a risk of error, we can wrap it in a *try* statement. If the *try* fails, then we can specify what should happen with the *except* keyword. Everything after the *except* statement will run as normal.

# In[58]:


try:
    1/0
except:
    print('Was not successful')
print('Code finished')


# The form of *except* above will work regardless of the kind of error. However, we can also specify the kind of error we want to avoid. A list of exceptions can be found [here](https://docs.python.org/3/library/exceptions.html)

# In[ ]:


try:
    2 + 'two'
except TypeError:
    print("can't mix these 2")


# A *try* statement can be combined with an *else* like *if*, and it can also include a *finally* statement - some code to run whether an exception occurs or not.

# In[67]:


x = 1
y = 'One' #try replacing 'One' with a number

try: 
    x + y
except TypeError:
    print("Type Error")
else:
    print("boo")
finally:
    print("end")


# ## Functions
# 
# Functions in Python are small scripts that accept a given group of objects (called *arguments*) as an input and produces another group of objects as output. It can be considered a generalisation of the kind of mathematical function $y = f(x)$ that you're familiar with from maths courses.
# 
# The anatomy of a function can be seen in the example below:

# In[9]:


a = 1
b = 3

def example_function(x,y):
    """
    comments on what the function does.
    Arguments:
    x -- a float value
    y -- a string
    """
    print(y)
    out = a*x**2 - b
    return out

z = example_function(2,'hey')
print(z)
print(x)


# Notice the following features:
# 
# #### The first line
# * the definition of a function begins with the *def* keyword
# * *def* is followed by the function name - it is conventional to use lower_case_and_underscores for function names in Python
# * after the function name we give a tuple of input values (also called parameters, or arguments when the function is called (not sure why there are multiple names for the same thing).
# 
# #### The main block of code
# * we can add some comments about what code will do using """triple quotes""" - this docstring comment can stretch over several lines, unlike normal # comments. Once you've created a function, you can check what the arguments should be by typing the function (example_function( ) and then pressing Shift+Tab to view the docstring comment. 
# * the block of code for the function is *indented* (one tab or four spaces) relative to the rest of the script. There has to be exactly this space for every line of the code, or it will not be interpreted successfully by Python.
# * the function can depend on variables defined in the preceding code (a,b) or the given arguments (x,y). 
# 
# #### The output
# * the output of the function is chosen by putting the *return* keyword before the output variables.
# * print(x) fails : the labels for the input value (e.g. x) are only used within the function definition, and are not variables in the main code.
# 
# #### Using the function
# * In Python, a function is *called* when it is used to assign values to a new variable (the line z = example_function...). 
# 
# ### Other features of functions
# * Optional parameters: we can assign default values to some parameters, in case they are not specified by the user

# In[18]:


def geom_mean(a,b=1):
    '''
    find the geometric mean of two numbers
    '''
    out = (a*b)**(0.5)
    return out
print(geom_mean(16))
print(geom_mean(16,4))


# * keyword parameters: we can choose a name, so the parameters don't have to be entered in the exact same order

# In[27]:


def weird_sum(a=0,b=0,c=0):
    return a + b - c
weird_sum(c=1,b=5,a=2)


# * functions can handle an unknown number of parameters, using the * prefix. The final set of parameters is in the form of a tuple

# In[37]:


def megaprint(str1,str2,*morestr):
    out1 = 'Hey ' + str1 + ' and ' + str2
    out2 = 'and ' + str(morestr)
    return out1,out2
y1,y2 = megaprint('Jack','Jill','Tom','Dick','Harry')
print(y1)
print(y2)


# ### Functional programming with lambdas
# 
# Another way to perform mathematical functions with Python is with [lambda expressions](https://docs.python.org/3.5/tutorial/controlflow.html#lambda-expressions). Lambda expressions are much more like regular maths functions you're used to, and are therefore more limited than regular functions, but can be handy for circumstances when you want a simple mathematical function. They are also useful for filtering (see below)

# In[43]:


y = lambda x: x**2 + 2*x + 1
print(y(2))


# ### Functions on lists
# #### Mapping
# Mapping can be used to apply a given operation to a list. It can therefore serve as a kind of function, provided the input is a list

# In[52]:


def quartring(a):
    return a/4
x = [1,2,3,4,5]
y1 = list(map(quartring,lst))
# or using lambda expressions
y2 = list(map(lambda x: x/4,lst))
print(y1)
print(y2)


# #### Filtering
# Filtering can be used to select certain items from a list, satisfying a given condition

# In[55]:


nums = range(-30, 35,5)
subzero = list(filter(lambda x: x < 0, nums))
print(subzero)


# ## More Python objects
# 
# The contents above should be enough for the practical - below are some more advanced topics which you can read about if you're interested.
# 
# * [Classes](https://docs.python.org/3/tutorial/classes.html) are more complicated code objects, one level above functions in the hierarchy. A particular *instance* of a class can have several functions within it. 
# * [Modules](https://docs.python.org/3/tutorial/modules.html) are Python scripts you can *import* into your current script so you can use the functions from the module without having to re-write the same code in your script. [Packages](https://docs.python.org/3/tutorial/modules.html#packages) (e.g. numpy, matplotlib) are examples of modules, but you can also import local .py scripts from your own computer.
