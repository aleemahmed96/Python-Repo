magician_list = ["chris","amil rustam bangali :D","bagali baba jharoo wale :D ","chote ustaad :P"]

def show_magician_name(names):
    """printing name of each magician in the list"""

    print('The magician names are:\n')
    for name in names:
        print(name.title())


def make_great(name):
    """putting 'the great' in list name"""

    for name1 in name:
        print("The Great",name1.title())

#make_great(magician_list)
        
#making copy of the original list
msg=[]
msg.append(make_great(magician_list[:]))
print(msg)

#showing original list
show_magician_name(magician_list)