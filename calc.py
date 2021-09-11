#keyfpenc11's first calc

import math

#

a = input ('Enter first number: ')
b = input ('Enter second number: ')
action = input ('Enter action (+, -, *, or /): ')

#

if action == '+':
	result = int(a) + int(b)
	print ('Result: ' + str(result))

if action == '-':
	result = int(a) - int(b)
	print ('Result: ' + str(result))

if action == '*':
	result = int(a) * int(b)
	print ('Result: ' + str(result))

if action == '/':
	result = int(a) / int(b)
	print ('Result: ' + str(result))