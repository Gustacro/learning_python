"""
file name: intro_dictionary

Purpose: Learn how to work with dictionaries.
	> create, update, delete, iterate, print

date: 01132020

key words: doctionary, dict, key, values

"""


# practice with dictionaries

# create a dictionary an empty dict
employee = {}

# add 3 employee and with name, age, position.
employee['Gustavo'] = [36, 'gis']
employee['Monica'] = [30, 'accountant']
employee['Jessica']= [32, 'teacher']


#------------ Create the same dictionary at ones -------------------

# Option 1
# employee = {'Gustavo': [36, 'gis'], 'Monica':[30, 'accountant'], 'Jessica':[32, 'teacher']}

# Option 2
# employee = dict(Gustavo = [36, 'gis'], Monica = [30, 'accountant'], Jessica =[32, 'teacher'])


# return the Gustavo's age
# print(employee['Gustavo'][0]) 

#--------------------- Iterate through the dictionary and return all the keys & values ------------
# for key , value in employee.items():
# 	print('key:')
# 	print(key)
# 	print('value:')
# 	print(value)
# 	print('')
# add to the dictionary employee: salary, race

#========================================================================

# Lets Update ONE value or MULTIPLE values from a dictionary

# Create a dictionary
student = dict(name = 'Gustavo', age = 36, courses= ['Math', 'Statistics'])

print('original dictionary...')
print(student)

# # lets change the student name
# student['name']= 'Jessica'
# # lets add a new key 'Phone', with its value
# student['phone'] = '555-5555'


# lets update multiple keys and its values:
student.update({'name': 'Jessica', 'age': 32, 'courses': ['Geography', 'History'], 'phone':'555-5555'})


# print dictionary
print('Dictionary updated')
print(student)


#---------------------- Delete or Pop a key and its value -----------------------
''' By using del function follow by a dict[<'key'>] this will delete the key '''

# del student['age']
print(student)

# now use pop(<'key'>) , This will remove the key and value from the table but will not delete it
age = student.pop('age')

print(student)

print(age) # to see the key that was pop

#----------- How to handle dictionary errors ----------------

''' 
let's try to find a key that does not exist in the employee dict using the get() method
'''
# print(student['last']) # This will return an error because this key does not exist in dict

# to return a None value 
print(employee.get('last')) 

# lets define the message in return:
print(employee.get('last', 'Not Found'))

#------------------------------ LOOP through the dictionary ---------------

# how many keys
print(len(student))

print(student.keys()) # see all the keys

print(student.values()) # see all the values

print(student.items()) # see all the keys and values

# loop through the keys
for key in student:
	print(key)

# loop through the keys and values
# solution 1
for key, value in student.items():
	print(key, value)

# solution 2
print([(key,value) for key,value in student.items()]) # using list comprehension 

print('__*' *20)
#------------------ ONLINE EXERCISES ----------------------------

# Exercises from : https://www.w3resource.com/python-exercises/dictionary/

# exercise 1:
# a: Write script to sort (ASC or DESC) dictionary by value

dict_1 = {3: 'c', 5: 'e', 2: 'b',  4: 'd', 1: 'a'}
print('Original Dictionary:\n \t', dict_1)

print()
print('Dictionary in ascending order by value')
for value in sorted(dict_1.values()):
	print('\t' ,value, end=" ")


# b: Write script to sort (ASC or DESC) dictionary by value
print()
print('dictionary in Descending order by value:')
sorted_dict_1 = [value for value in sorted(dict_1.values(), reverse = True)]
print('\t', sorted_dict_1)


#======================================================
# exercise 2:
# add a key to a dict_1:

dict_1['name']= 'Bebe'
print('dictionary updated\n')
print(dict_1)


#=====================================================
print()
# exercise 3: 
# Script to concatenate the following dictionaries:
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

main_dict= {} # create empty dictionary
for d in (dic1, dic2, dic3): main_dict.update(d) 
print('Nested Dictionary:\n', main_dict)


#=========================================================
# exercise 4:
# check if given key already exists in dictionary

employee = {'name': 'Maria', 'age': 26, 'phone': '555-5555'}

# check if key exists
def if_exists(dict, key):
	if key in employee.keys():
		print(f'the key {key} does exists in employee dictionary')

	else:
		print(f'The given key {key} does not exists in the employee dictionary')

# define key to check for 		
key = 'name'
# run function
print(if_exists(employee, key))