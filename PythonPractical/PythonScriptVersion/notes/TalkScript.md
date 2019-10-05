#Introduction to Python Supervisor Script

Thomas Parton, 180926

## Introduction

### Why choose to learn Python?

#### Why learn programming at all?

Scripts written in Python can be used to perform virtually any conceivable computer task. In particular, it is very popular for data analysis, data visualisation (plotting), computer task automation, numerical simulation and modelling. As a result Python is widely used in scientific computing, data science, finance and elsewhere.

#### Why learn Python instead of some other programming language?

##### It’s easy to use

- Free and open-source
- Relatively easy to learn (compared to other languages)
- Readable code (high-level language)
- Robust and error-tolerant

##### It's powerful

- Versatile (multiple programming paradigms)
- Extensible (easy to upgrade what it can do

##### It’s popular

- Active online support community 
- A lot of other people already use it. 

### Other info

The instructions in this practical assume you are using Python on a Microsoft Surface Pro operating Windows 10. The instructions for other systems (Mac, Linux etc.) will be slightly different, but they can readily be found online.

### How Python works

You as the user have an idea of some task you want to complete. Let's say you want to add together two numbers. You arrive with some inputs (a,b) and some operation you want to perform (+) to produce a given output (a+b). Obviously in this simple example you know clearly what needs to be done, but in other cases the operations are much more complex (e.g. plotting a given set of data, adding trendlines etc.). 

As a human you speak a natural language (English). You know that English has a particular grammar (a set of correct ways in which words can be combined into sentences) as well semantics (a relationship between sequences of words and some abstract meaning).

The same is true for programming languages, including Python. There is a syntax (grammar) which relates sections of code, and some combinations have meaning and others do not.

-  "Colourless green ideas sleep furiously" (correct syntax, no meaning)
- "The King of France is bald".  (syntax and meaning, but no output)

You write Python source code (lines and lines of code) into a source code editor (Notepad), making sure you code is correct for syntax and semantics. Typically the editor is part of a larger IDE, so there's a debugger etc. to check your code makes sense. 

#### Implementation of Python

Implementation = a way in which Python code can be read, understood and acted upon by the computer.

The standard version of Python is written in C (another, more fundamental programming language). CPython is an interpreted language (meaning that instructions are directly converted into machine code to be performed on the CPU).

Python contrasts with a compiled language (such as LaTeX or some implementation of Python, see later). Here the code is "compiled" and then later "run". 

#### Python development environments 

IDE - integrated development environment (combines source code editor, debugging functions, colour-coding)

standard is IDLE (integrated development and learning environment) [show IDLE]

#### Command line versus other intepretation

Py Shell for IDLE - REPL (read, evaluate, print loop) (compare to Windows Command Prompt)

#### Comparison of IDEs

See wiki https://en.wikipedia.org/wiki/Comparison_of_integrated_development_environments#Python

#### Python distributions

- Main disitribution (CPython, with pip etc.)
- Anaconda (conda, Python and R) https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)

###Final things to be aware of

#### Versions of Python 

There's Python 2 (ending 2.7) and Python 3 (still active).

example: Python 2 (top) and Python 3 (bottom)

```python
print 'hey gorgeous'
```

```python
print('hey gorgeous')
```

More egregious examples: https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html

#### Jupyter notebooks

Not just about Python - also works for R (data science) and other languages.

REPL-type Python interpreter based in a web browser. WOrks on chunks of code at a time, not just single lines.

Similar to Wolfram Mathematica or Maple notebooks 



## Python core syntax

Can't explain everything now: stick to glossary and simple explanations

- numbers = int integers, float, complex
- strings = sequence of characters (char). str = 'hey gorgeous'
- indices (start at 0) str[0] = 'h'
- lists and tuples - sets of objects list [] can be int, float, strings. tuple (). can't assign new values to tuples. can make new tuples. tuple for heterogeneous collection. tuples are faster.
- dictionary dict : keys and values, pair is an item
- function. mathematical style, input and output. lowercase underscore convention
- classes MyClass convention. set of methods (functions inside classes). Instance of a class
- exceptions (getting around potential errors )

#### Extensions - modules and packages

module = any py source code file (including ones you make yourself). typically a single entity.

package = collection of .py files, containing many modules

pip, awareness of conda

### Useful packages

Display all the packages you currently have installed using

```powershell
pip list
```

- SciPy https://www.scipy.org/
  - NumPy http://www.numpy.org
  - Matplotlib
  - pandas (data analysis and visualisation)
  - Sympy (symbolic maths)
- re and regex for regular expressions
- Pillow for image manipulation https://python-pillow.org/
- Date and time work: python native datetime or Pendulum https://github.com/sdispater/pendulum
- GUIs
  - https://wiki.python.org/moin/PyGtk PyGtk
  - https://wiki.python.org/moin/PyQt PyQt
  - https://wiki.python.org/moin/TkInter Tkinter

[SciPy topical software list](https://scipy.org/topical-software.html#head-b98ffdb309ccce4e4504a25ea75b5c806e4897b6) 

Comprehensive general list https://github.com/vinta/awesome-python

#### Graphical user interfaces (GUIs)

If you want to construct a GUI (with windows, buttons and displays) the three most common implementations are [PyQt](https://wiki.python.org/moin/PyQt), [tkinter](https://wiki.python.org/moin/TkInter) and [PyGtk](https://wiki.python.org/moin/PyGtk). In my experience PyQt is the most commonly used. 



#### Further common Py syntax from packages

NumPy

- extended set of data types (int8, float32)
- arrays (vectors and matrices) np.array([1,2,3,4])
- structured arrays (fields https://docs.scipy.org/doc/numpy/user/basics.rec.html )

Matplotlib

- axes, plot, subplot

Pandas

 http://nbviewer.jupyter.org/github/jvns/pandas-cookbook/blob/v0.2/cookbook/Chapter%201%20-%20Reading%20from%20a%20CSV.ipynb

- data frame versus database

NumPy for MATLAB users : https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html







## Good coding habits

Comparison to good lab practice

- Think before you type
- Make a sketch of what the code will do and break it down into individual tasks.
  ​    

| Good coding habit                                            | Good lab habits                                              |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Make a plan of what the code will do and break it down into individual tasks. | Make a plan of what the experiment will do and break it down into smaller tasks. |
| Label objects (e.g. functions) in a consistent way           | Label samples in a consistent way                            |
| Add concise, useful comments to make the code easier to read | Add concise, useful observations about the experiment to make the lab book easier to read |
| Don't overfill a line                                        | Don't overfill a line                                        |
| If things are going wrong, check individual sections of code one at a time | If things are going wrong, check individual components of the equipment one at a time |
|                                                              |                                                              |

#### Commenting well

- Comment well. The reader will probably be a stranger (e.g. future you)
- write a comment to explain what an object is doing, if it's not obvious
- Provide info when defining a function (e.g. what it does, what input data types are, what outputs are)
- Don't write obvious comments (just clutter the page up)

####Naming well

- Intuitive and consistent naming/labelling
-  functions, classes, eg all defined in similar ways
-  obvious names which can't be confused. Also comment when name is defined
- Avoid setting and getting]

####Large-scale code structure

- group together similar actions (e.g. loading and saving files)

####Overall project structure

- organise your files (e.g. raw data in one sub-directory, cleaned in another, scripts in another)

#### Other good habits

- make ideal chunks of code for yourself to use later (e.g. a generic plot of data, converting data types)
- Organising your folder structure to fit your purpose (eg. raw data in one folder, processed in another, code in a third)
- Refactoring (read your code at the end, clean it up, add comments). Same as reading back over your lab book at the end of the experiment to check you included everything useful.
- Test code on simple examples at many stages instead of doing everything in one go (e.g. print outputs)

#### Examples of good coding

- Open source code projects are usually an example of good practice.
- PEP8 https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds

##Debugging code

- Read what the error message says - sounds obvious but it usually gives you an idea of what's going on.
- Handling exceptions
- Print intermediate outputs (sanity checking)



## Learning Python

Useful links
​    Step-by-step for Python (e.g. Python the hard way)
​    Sololearn for Python 3: https://www.sololearn.com/Course/Python/
​    https://docs.python-guide.org/



## Finding solutions to your Python problems

### How to find solutions

- Reading the official documentation
- Online search (i.e. whatever appears on google)
- Talking to people (working through, articulating your problem helps)

#### Official documentation

Official documentation for Python or associated packages. Like an encyclopaedia, comprehensive but dense. Rather than reading the full page I tend to skip down to the examples. Main examples:

- https://docs.python.org/3/ For the core Python program
- SciPy/NumPy manuals https://docs.scipy.org/doc/numpy/index.html
- https://matplotlib.org/ Matplotlib official documentation

#### Unofficial sources

- [Stack Overflow](http://stackoverflow.com/) is a website where anyone can post their programming questions. Anyone can respond, and other users vote on the responses so that (in theory) the best response rises to the top. [Example: ](https://stackoverflow.com/questions/36878089/python-add-a-column-to-numpy-2d-array?noredirect=1&lq=1) adding a column to a 2D NumPy array 
- GitHub (online repositories of code). Example for learning Python with Jupyter notebooks: https://github.com/jerry-git/learn-python3/blob/master/README.md
- Whatever comes up when you type your problem into a search engine (blogs, online forums)

Advice on finding solutions online

- Identify the core issue you want to solve
- Define the question precisely to get to the right answer more quickly - use the correct language (e.g. class, module, array)
- Check any code copied off a website by running it on your computer before incorporating it into your code.



#### Talking to people

Some people find it helpful to talk through their coding problems with other people. THe act of articulating your problem may help you figure out where things are going wrong. 

Greg - fixing his own problems.



### Is it wrong to use code from a website?

[consider moving to 'good' code section]

What do you want from your code? 'Good' code can be described as

- effective (it does the task you want it to do)
- user-friendly (readable and well-commented)
- quick to write or use (so you can finish coding and get on with doing real experiments)
- efficient (it does the task as quickly as possible and has no unnecessary parts)
- original (something you created yourself)

The ordering here is my personal order of preference. You can see that Originality is at the bottom. I'm not a computer scientist and I don't take particular pleasure in coding, but I want something that works well. I suspect your own order of preference for code qualities may be similar.

[end]

No, if you do it intelligently and conscientiously.

You are expected to produce code that can reasonably be described as your own work. You should understand every single line of code (what it does, the inputs and outputs, the data types etc.). However, it doesn't mean that everything in the code is original, and you will almost certainly use online sources (official documentation, online forums, and others). 

You shouldn't directly copying and pasting code from a website, partly because it's immoral to plagiarise someone else's hard work, but mainly because it's stupid. You're unlikely to find an exact solution to your problem online, so rather than pasting in their code and hoping for the best, figure out if their code does what you want to do and adapt it to your purpose. By doing this you will probably end up completing re-writing the code from scratch with significant alterations, and by doing so the code can fairly be considered your own work.

A good procedure for using code from elsewhere:

- copy the code into a separate python file
- run the code. Figure out how it works, and whether it does the task you want
- 

Python is open-source (as are many programming languages), so anything written in official documentation online is free to use without copyright. The same applies to Python extensions (i.e. packages). Code written in other places (e.g. GitHub) is also likely to be free from copyright, although you should double-check. 

If you want to use someone else's code (e.g. a particular tool), or the code is particularly ingenious in a way you don't think you would've discovered otherwise, then you can add a hyperlink/reference to the source in the commenting of the file. https://en.ru.is/referencing/plagiarism/computer-code/



When publishing academic papers, it's not common to cite Python packages, although some authors do (see e.g. https://www.nature.com/articles/nature13802).



or share your original code.





From a legal perspective, you are also fine. The University of Cambridge does include computer code in their broad definition of plagiarism https://www.plagiarism.admin.cam.ac.uk/what-plagiarism/universitys-definition-plagiarism. However, 

If you plan to commercialise your code, rather than using it purely for academic purposes, you will need to 





Good practice for using code from other sources

- never use copied code without further alteration
- understand every line of the code (what it does, inputs and outputs). 
- re-write the code with new variable names (this does not change the fact that it's plagiarised)
- change the structure to fit your own needs (avoid making a Frankenstein's monster). Data types, inefficient code
- if you want to use a substantial piece of code (>200 lines) verbatim, or the code is particularly ingenious in a way you don't think you would've discovered otherwise, then you can add a hyperlink/reference to the source in the commenting of the file. https://en.ru.is/referencing/plagiarism/computer-code/
- using a package is not plagiarism
- in general, useful to comment in a link

- 























##Links to other software

- MATLAB [MATLAB](https://www.mathworks.com/help/matlab/matlab_external/connect-python-to-running-matlab-session.html) and https://stackoverflow.com/questions/2255942/how-do-i-interact-with-matlab-from-python
- Origin Lab - PyOrigin module and https://www.originlab.com/doc/python/Run-Python-in-Origin
- Jython http://www.jython.org/Project/
- Python-Java interface https://wiki.python.org/moin/ScriptingJava
- Arduino serial port, PySerial, see also https://gitlab.com/william.belanger/bridge, full link in development http://inotool.org/
- Simualte mouse movement https://github.com/boppreh/mouse and keyboard typing https://github.com/boppreh/keyboard
- http://www.pingo.io/docs/ Raspberry Pi
- ImageJ - Jython to write attachments for IMageJ http://imagej.net/Jython_Scripting
- OneNote https://developer.microsoft.com/en-us/onenote



#### VPython

- examples http://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/

### Labview

 •Python and labview 

•Python API for labview (NI program) [http://www.ni.com/white-paper/53059/en](http://www.ni.com/white-paper/53059/en/)[/](http://www.ni.com/white-paper/53059/en/)

•[https://nimi-python.readthedocs.io/en/master](https://nimi-python.readthedocs.io/en/master/)[/](https://nimi-python.readthedocs.io/en/master/)

Examples [https://](https://github.com/ni/nimi-python/tree/master/src/nidmm/examples)[github.com/ni/nimi-python/tree/master/src/nidmm/examples](https://github.com/ni/nimi-python/tree/master/src/nidmm/examples)

[https://](https://pyvisa.readthedocs.io/en/stable/getting.html)[pyvisa.readthedocs.io/en/stable/getting.html](https://pyvisa.readthedocs.io/en/stable/getting.html) pyvisa for visa https://www.ni.com/visa/

•[https://myopenlab.org/inicio](https://myopenlab.org/inicio/)[/](https://myopenlab.org/inicio/) - seems to be Java

•[https://sourceforge.net/projects/pylab-works](https://sourceforge.net/projects/pylab-works/)[/](https://sourceforge.net/projects/pylab-works/) (last update 2015)

​    t







## Conclusions

Conclusions/Feedback
​    Not a comp sci, make code that works





## Misc Notes

#### Other links

Google colab https://colab.research.google.com/notebooks/welcome.ipynb Free jupyter notebook online for ML.



Useful chunks of code
​    Extract .txt files from a given folder (using os)
​    Finding a particular line in a file
​    Finding a particular text pattern (regex)
​    Searching for a solution on Stack Overflow
​    processing batches of files from a folder useful.

### Useful packages

Display all the packages you currently have installed using

```powershell
pip list
```

- SciPy https://www.scipy.org/
  - NumPy 
  - Matplotlib
  - pandas (data analysis and visualisation)
  - Sympy (symbolic maths)
  - IPython
- re and regex for regular expressions
- Pillow for image manipulation https://python-pillow.org/
- Date and time work: python native datetime or Pendulum https://github.com/sdispater/pendulum
- GUIs
  - https://wiki.python.org/moin/PyGtk PyGtk
  - https://wiki.python.org/moin/PyQt PyQt
  - https://wiki.python.org/moin/TkInter Tkinter



Comprehensive general list https://github.com/vinta/awesome-python

## During the practical

### Blocks

I know that most of you are relatively new to Python. A practical where you learn the "grammar" of Python (functions, modules, classes etc.) would be quite dry and dull. Therefore I'm going to give you some working pieces of code for you to play with. 

Example: plotting a simple histogram of data in a given format.

### Challenges

Now I will give you a series of challenges to attempt, by combining the blocks together.

The challenges are model examples of problems you may want to solve using Python during your research. 

The challenges vary in difficulty, indicated by the number of chilis next to the title.

During the practical, try the challenges. I will float around and supervise, answer questions etc. I also recommend you try solving your own issues using StackOverflow.

```
Stack Overflow http://stackoverflow.com/ 
Reddit https://www.reddit.com/r/Python/ (see RH tab for resources)

Regex: http://regex101.com/
Also regex crosswords https://regexcrossword.com/
```

