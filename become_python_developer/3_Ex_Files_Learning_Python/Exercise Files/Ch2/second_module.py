
# By running the -- import <module's_name> -- it will print any code that's outside of the function from the imported module in this case (first_module.py). 
import first_module 

'''
this will print second module name which in this case is __main__ because calling directly from this script 
'''

# if you want to run the the main method form first_module.py you can do:
first_module.main()

print("Second Module's Name: {}".format(__name__))
