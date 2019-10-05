#!/usr/bin/env python
# coding: utf-8

# # File Management with os and shutil
# *See end of notebook for useful information (glossary of terms and syntax).*
# 
# Example files and folders are in the '.\os_examples' sub-folder of the block notebooks folder.
# 
# * operations on paths
# * operations on directories
# * operations on files

# In[17]:


import os
import shutil


# ## Operations for paths
# https://docs.python.org/3/library/os.path.html

# ### Check a path exists

# In[67]:


src = '.\os_examples'
print(os.path.exists(src))


# ### Find the absolute path (of a given relative path)

# In[57]:


pth = '.\\block notebooks\\os_examples'
os.path.abspath(pth)


# ### Find the basename and directory name (of a file path)
# 

# In[52]:


# source = src
src = '.\\block notebooks\\os_examples'
# Get basename
print(os.path.basename(src))
print(os.path.dirname(src))


# ### Joining together bits of a path
# The os.path.join() function will intelligently join together path elements:
# * it will add in backslashes if they're missing (see first example)
# * it assumes anything with a backslash in front is a dir (see second example)

# In[47]:


bit1 = r'C:\dir'
bit2 = 'file.jpg'
path1 = os.path.join(bit1,bit2)
print(path1)

bit3 = r'\file.jpg'
path2 = os.path.join(bit1,bit3)
print(path2)


# ## Operations for directories
# See also [Python os manual](https://docs.python.org/3/library/os.html)
# ### Identifying the current working directory

# In[35]:


# get cwd = current working directory
cwd = os.getcwd()
print(cwd)


# ### Change the cwd

# To change the cwd, use os.chdir(). This is in comments so you don't change the cwd and screw up the rest of the notebook.

# In[20]:


# new_cwd = 'C:\\'
# os.chdir(new_cwd)
# print(os.getcwd())


# ### Creating a directory
# A new dir (folder) can be made using the os.mkdir() function. If the input is a string (e.g. os.mkdir('my_new_folder'), the new dir is made in the current working directory. A new dir can be made in any location in the file system by specifying the absolute or relative path.

# In[48]:


#Choose new dir location
newdir = r'.\os_examples\new_dir'
os.mkdir(newdir)


# ### Delete a directory

# In[49]:


# Specify directory location
deldir = r'.\os_examples\new_dir'
os.rmdir(deldir)


# ### Rename a directory

# In[61]:


src = r'.\os_examples\oldname_dir'
dst = r'.\os_examples\newname_dir'
os.rename(src,dst)
# check path exists (returns true)
print(os.path.exists(dst))


# ### List all contents of directory

# In[63]:


src = r'.\os_examples'
print(os.listdir(src))


# ## Operations for files
# See also os manual and [shutil manual](https://docs.python.org/2/library/shutil.html
# )
# 
# Reading and writing to files is covered in a separate block.
# 
# ### Delete a file

# In[66]:


src = r'.\os_examples\to_delete.png'
# uncomment and run to delete the file
# os.remove(src)


# ### Rename a file
# Same as renaming a directory (os.rename, see example above)

# ### Copying a file
# The destination can be
# * a file name (the file is copied to the given location and takes the new name)
# * a dir (the file is copied to the dir with its original name

# In[54]:


# source
src = r'.\os_examples\copy_src.txt'
# destination
dst1 = r'.\os_examples\new_location.txt'
dst2 = r'.\os_examples\random_dir'

# copy to file
shutil.copy(src,dst1)
# copy to dir
shutil.copy(src,dst2)


# ## Useful information
# ### File management glossary
# 
# #### basename
# The "short name" of the object described by the path. For a file, it's the short filename (e.g. image.png). For a folder, it's the short folder name (e.g. My Pictures)
# #### current working directory:
# The current working directory (cwd) is the current active folder where Python/Jupyter is operating. The os package can be used to identify it (see above).
# #### directory (dir)
# Another name for a folder (a path containing collection of paths to files or subdirectories)
# #### path
# The unique location of the file in the computer's file system. Example: the Downloads folder on Windows, C:\Users\USERNAME\Downloads
# 
# ### File name syntax in Windows and Python
# * In Windows (unlike other operating systems), the subdirectories in a path are separated by a backslash \. In Python 
# * Raw [string literal](https://docs.python.org/2/reference/lexical_analysis.html#string-literals) - add lowercase 'r' in front of the string (e.g. r'like this')
# 
# ### Absolute and Relative paths
# The path to a file or dir can be *absolute* or *relative*. 
# * An *absolute* path is a full path from the base dir, usually the local disk (C:). 
# * A *relative* path tracks the path relative to the current working directory
# 
# As an example, in the block folder is a sub-directory called 'os_examples'. 
# * The absolute path is 'YOURSYSTEM\block notebooks\os_examples'
# * The relative path (from YOURSYSTEM\block notebooks) is '.\os_examples'
# 
# Syntax for relative paths:
# * a single dot '.' is used to represent the cwd. 
# * a double dot '..' represents the superfolder (ie. the folder of which the cwd is a subfolder)

# In[ ]:




