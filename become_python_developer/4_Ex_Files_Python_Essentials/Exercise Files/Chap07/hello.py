#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def func1(func3):
	def func2():
		print('This is before the function call')
		func3()
		print('This is after the function call')
	return func2


def func3():
	print('This is func3')


x = func1(func3)
x()