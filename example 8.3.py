
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


