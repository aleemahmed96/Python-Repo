#Using a program you wrote that has one function in it, store that
#function in a separate file. Import the function into your main program file, and
#call the function using each of these approaches:
#import module_name
#from module_name import function_name
#from module_name import function_name as fn
#import module_name as mn
#from module_name import *

#CAUTION: also see for 'print_models.py' file inside of github,it may not work 
# if you didn't get that file in the same path as for this program.


#import module_name as mn
import print_models as pm
cake= ['polygon','square','rectangle']
vanilla = []
pm.print_models(cake,vanilla)
    #cake and vanilla are callsign for the "unprinted_designs" and "completed_models" respectively.
pm.show_completed_models(vanilla)


#import module_name
import print_models
cake= ['polygon','square','rectangle']
vanilla = []
print_models.print_models(cake,vanilla)
print_models.show_completed_models(vanilla)


#from module_name import function_name
from print_models import print_models,show_completed_models
cake= ['polygon','square','rectangle']
vanilla = []
print_models(cake,vanilla)
show_completed_models(vanilla)


#from module_name import function_name as fn
from print_models import print_models as pm
cake= ['polygon','square','rectangle']
vanilla = []
pm(cake,vanilla)
from print_models import show_completed_models as cm
cm(vanilla)


#from module_name import *
from print_models import *
cake= ['polygon','square','rectangle']
vanilla = []
print_models(cake,vanilla)
show_completed_models(vanilla)