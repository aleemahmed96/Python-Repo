""" A Python dictionary can be used to model an actual dictionary.
    However, to avoid confusion, let’s call it a glossary.
    • Think of five programming words you’ve learned about in the previous
    chapters. Use these words as the keys in your glossary, and store their
    meanings as values.
    • Print each word and its meaning as neatly formatted output. You might
    print the word followed by a colon and then its meaning, or print the word
    on one line and then print its meaning indented on a second line. Use the
    newline character (\n) to insert a blank line between each word-meaning
    pair in your output.
"""

glossary = {}
glossary['list'] = 'data structure that is mutable, or changeable, ordered sequence of elements'
glossary['string'] = 'data type that defines string' 
glossary['int'] = 'data type that defines integer value'
glossary['dict'] = 'unordered values accessed by key rather than by index'
glossary['function'] = 'block of organized, reusable code that is used to perform a single, related action'

print('\n\"Defination\" \n')
print("list : " + glossary['list'] + ".")
print("string : " + glossary['string'] + ".")
print("int : " + glossary['int'] + ".")
print("dict : " + glossary['dict'] + ".")
print("function : " + glossary['function'] + ".")

#it will be used for exercise 6.4
"""
for key,value in glossary.items():
    print ("\'" + key + "\'" + " : " + "\'" + value + "\'" + "\n")
"""