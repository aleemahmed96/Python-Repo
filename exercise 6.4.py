"""
Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
"""

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
