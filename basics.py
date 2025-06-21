print("pooja")
#this is single line comment
"""this is multiline comment"""
print("multiline commenting")
#datatypes
a =5
print(type(a))
b = 3.0
print(type(b))
c="pooja" #In Python, there's no separate char type. A single character is a string of length 1.
print(type(c))
d =True
print(type(d))
e=123.456 #In Python, float and double are the same (float).
print(type(e))
#global and local scope
number = 100  # Global variable

def show_scope():
    number = 50  # Local variable
    print("Local variable:", number)         # Prints 50
    print("Global variable:", globals()['number'])  # Prints 100

show_scope()