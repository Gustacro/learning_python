#
# Example file for working with classes
#


class myCLass():
	def method1(self):
		print('myCLass method1')

	def method2(self, someString):
		print('myCLass method2', someString)


class anotherClass(myCLass): # anotherClass is going to inherit from 'myClass'
	def method1(self):
		myCLass.method1(self)
		print('anotherClass method1')
		

	def method2(self, someString):
		print('anotherClass method2')

def main():
	c= myCLass()
	c.method1()
	c.method2('This is a string')

	# Instance of another Class
	c2 = anotherClass()
	c2.method1()
	c2.method2('This is a string')
	

if __name__ == "__main__":
	main()
