# practice with dictionaries

# create a dictionary an empty dict
employee = {}

# add 3 employee and with name, age, position.
employee['Gustavo'] = [36, 'gis']
employee['Monica'] = [30, 'accountant']
employee['Jessica']= [32, 'teacher']


# Create the same dictionary at ones 

# Option 1
# employee = {'Gustavo': [36, 'gis'], 'Monica':[30, 'accountant'], 'Jessica':[32, 'teacher']}

# Option 2
# employee = dict(Gustavo = [36, 'gis'], Monica = [30, 'accountant'], Jessica =[32, 'teacher'])


# return the Gustavo's age
# print(employee['Gustavo'][0]) 

# Change age for Jessica
employee['Jessica'][0] = 30

# Iterate through the dictionary and return all the keys & values 
# for key , value in employee.items():
# 	print('key:')
# 	print(key)
# 	print('value:')
# 	print(value)
# 	print('')
# add to the dictionary employee: salary, race


# change values from the employee dict


# delete values from employee dict 


# delete employee from employeee dict


#----------- How to handle dictionary errors ----------------

''' 
let's try to find a key that does not exist in the employee dict using the get() method
'''
# print(employee['Tom']) # with this you will get an error because this key does not exist in dict

# to return a None value 
# print(employee.get('Tom')) 

# lets define the message in return:
# print(employee.get('Tom', 'Not Found'))


