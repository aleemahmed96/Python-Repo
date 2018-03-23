#making a program (by function) to read contents in a file (silently)
def show_content(filenames):
    """Showing the contents of the file"""
    try:
        file = open(filename,"r")
        contents = file.readlines()
    except FileNotFoundError:
        pass
    else:
        #just wanted to make it for myself
        for spelling in contents:
            print(spelling)
            print(len(spelling))

filenames = ["cats.txt","dogs.txt"]
for filename in filenames:
    show_content(filename)