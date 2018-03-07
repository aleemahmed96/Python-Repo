#Write a function called make_shirt() that accepts a size and the
#text of a message that should be printed on the shirt. The function should print
#a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the
#function a second time using keyword arguments.

def make_shirt(size,text):

    """[making a function to show the size and text that should be printed on shirt]
    
    Arguments:
        size {string} -- [XS,S,M,L,XL]
    """

    print("This shirt is " + size + "." + text)

#when using by positional arguments    
make_shirt("XS"," Happy Valentines Day")

#when using by keyword arguments
make_shirt(size="XL",text=" This shirt is too big.")       


