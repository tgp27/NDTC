#!/usr/bin/env python
# coding: utf-8

# # Reading and Writing Files
# Example text files are in the '.\rw_examples' sub-folder.
# 
# * Basic Python
#     * Reading from file
#     * Writing to file
# * Pandas
#     * Reading using read_csv
#     * Writing using to_csv
# 
# ## Basic Python
# Text used is taken from Article 1 of the UN [Universal Declaration of Human Rights](http://www.un.org/en/universal-declaration-human-rights/)
# ### Reading from file
# There are two ways to do this in basic Python:
# * open a file, read, then close the file again (separate steps)
# * use the "with" keyword to open, read and close automatically
# 
# "With" is preferred for reading because the file is automatically closed when it's finished being used.

# In[28]:


src = r'.\rw_examples\un_dec_art1.txt'

# Method 1
file = open(src,'r+')
fstr1 = file.read()
print(fstr1)

# Method 2
with open(src) as file:
    fstr2 = file.read()
print(fstr2)


# #### Selective reading

# In[15]:


src = r'.\rw_examples\un_dec_art1.txt'

with open(src) as file:
    # read the first 20 chars
    short_str = file.read(20)
    # read the rest of the file
    long_str  = file.read()
print('First string:')
print(short_str)
print('And the second string:')
print(long_str)


# #### Reading specific lines
# Just the first line

# In[19]:


src = r'.\rw_examples\un_dec_art1.txt'

with open(src) as file:
    line1 = file.readline()
print(line1)


# Get all lines as a list of strings - this can be used to obtain specific lines

# In[21]:


with open(src) as file:
    lines = file.readlines()
print(lines)
line3 = lines[2]
print(line3)


# ### Writing to file
# Syntax:
# * \n indicates a line break (new line)
# * \t indicates a tab space

# In[26]:


dst = r'.\rw_examples\new.txt'
content = "Here's some text\t I'd like to add\n to the file"
print(content)

file = open(dst,"w+")
file.write(content)
file.close()


# ## Pandas

# ### Reading numerical data using pandas
# Pandas has a read_csv module which makes it easy to import .csv data. It also works for .txt files.

# In[27]:


import pandas as pd

src = r'.\rw_examples\abso_data.txt'
df = pd.read_csv(src,sep='\t',header=None)
# add column names
df.columns = ['Wavelength','Absorbance']
# show first 5 values
df.head()


# ### Writing or appending data to file using pandas
# Writing to a file means either creating a new file, or deleting what is previously there and putting new content.
# 
# Appending means adding new data to existing data.

# In[36]:


dic = {'col1': [1,2,3], 'col2': [1,4,9]}
df = pd.DataFrame(data=dic)

dst = r'.\rw_examples\new_data.txt'
df.to_csv(dst,sep='\t')

# APPEND using 'a' form of open()
dic2 = {'col1': [4,5,6], 'col2': [6,25,36]}
df2 = pd.DataFrame(data=dic2)

with open(dst, 'a') as file:
    df2.to_csv(file,sep='\t',header=False)


# ### References
# * Read and write section of the [Python manual](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
# * Pandas manual

# In[ ]:




