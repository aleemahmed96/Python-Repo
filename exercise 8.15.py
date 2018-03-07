#Put the functions for the example print_models.py in a
#separate file called printing_functions.py. Write an import statement at the top
#of print_models.py, and modify the file to use the imported functions.

#CAUTION: also see for 'print_models.py' file inside of github,it may not work 
# if you didn't get that file in the same path as for this program.


#three ways to use import function are as follows:

    #import print_models
    #import print_models as pm
    #from print_models import *
#use any of them as your preference and which suit your style.

import print_models as pm

cake= ['polygon','square','rectangle']
vanilla = []
pm.print_models(cake,vanilla)
    #cake and vanilla are callsign for the "unprinted_designs" and "completed_models" respectively.
pm.show_completed_models(vanilla)
