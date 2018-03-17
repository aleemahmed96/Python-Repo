""" Start with Exercise 6-4 (page 108), where you
    used a standard dictionary to represent a glossary. Rewrite the program using 
    the OrderedDict class and make sure the order of the output matches the order
    in which key-value pairs were added to the dictionary.
"""
from collections import OrderedDict

glossary = OrderedDict()
glossary = {}
glossary['list'] = 'data structure that is mutable, or changeable, ordered sequence of elements'
glossary['string'] = 'data type that defines string' 
glossary['int'] = 'data type that defines integer value'
glossary['dict'] = 'unordered values accessed by key rather than by index'
glossary['function'] = 'block of organized, reusable code that is used to perform a single, related action'
glossary['class'] = "A user-defined prototype for an object that defines a set of attributes that characterize any object of the class"
glossary['method'] = "function that is made inside the class"
glossary['call'] = "a call is a procedure that links to the repective address of function,method or class"
glossary['instance'] = "any object tha is associated with class"
glossary['docstring'] = "used to define and explain function,methods and classes"

for key,value in glossary.items():
    print ("\'" + key + "\'" + " : " + "\'" + value + "\'" + "\n")
