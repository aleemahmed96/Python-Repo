magician_list = ["chris","amil rustam bangali :D","bagali baba jharoo wale :D ","chote ustaad :P"]

def show_magician_name(names):
    """printing name of each magician in the list"""
    print('The magician names are:\n')
    for name in names:
        print(name.title())
    
show_magician_name(magician_list)