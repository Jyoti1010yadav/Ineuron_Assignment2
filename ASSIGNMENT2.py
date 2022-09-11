'''10. Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
 9:00 PM)'''
import datetime
DATE=datetime.date.today()
Date=DATE.strftime("%d-%m-%Y")
print("DATE",Date)
TIME=datetime.datetime.now()
Time=TIME.strftime("%H:%M")
print("TIME",Time)
print()

'''1. Write a python script to add comments and print “Learning Python” on screen.'''

'''this is comment'''
print('"Learning Python"')
print()

# 2. Write a python script to add multi line comments and print values of four variables each in a new line. Variable contains any values.
'''this is 
multiple 
line comments
'''
var1="jyoti"
var2=12.5
var3=56
var4=1+3j
print(var1,var2,var3,var4,sep="\n")
print()

'''3. Write a python script to print types of variables. 
Create 5 variables each of them  containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)'''

var1=35
var2=True
var3="MySirG"
var4=5.46
var5=3+4j
print(var1,type(var1))
print(var2,type(var2))
print(var3,type(var3))
print(var4,type(var4))
print(var5,type(var5))
print()
# 4. Write a python script to print the id of two variables containing the same integer values.
var=1
Var=1
print("var",id(var))
print("Var",id(Var))
print()
''' 5. Create four variables in a Python script and assign values of different data types to them.
Write a Python script to print value, its type and id of each variable'''
var1=35.5
var2=False
var3="My"
var4=5
var5=3+4j
print(var1,type(var1),id(var1))
print(var2,type(var2),id(var2))
print(var3,type(var3),id(var3))
print(var4,type(var4),id(var4))
print(var5,type(var5),id(var5))
print()
# 6. Write a python script to print all the keywords
import keyword 
print("Keywords",end="\n")
print(keyword.kwlist)
print()
# 7. On Python shell use help() function and display the list of keywords
'''>>> help()
help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               break               for                 not
None                class               from                or
True                continue            global              pass
__peg_parser__      def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
'''

'''8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some value to it. 
Write a python script to import A1 module in A0 and print value of the variable created in A0.py

solution:- In A1 we make variable of name "variable_name_of_A1 " and A0 we write this below code

import A1
print(A1.variable_name_of_A1)

'''

''' 9. Name the keywords, used as data in the Python script.
solution:-
True,None,False are three keywords used as data in python script 

'''
