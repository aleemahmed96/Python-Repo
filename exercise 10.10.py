def count_words(filename):
    """Showing the contents of the file"""
    try:
        file = open(filename,"r")
        contents = file.read()
    except FileNotFoundError and UnicodeDecodeError:
        pass
    else:
        word = contents.lower().count("the")
        print("The word \'the\' is found to be: " + str(word))

#problem got when my text file was at UTF-8 encoding,
#so I change it to ANSI encoding.

filename = "gutenberg.txt"
count_words(filename)